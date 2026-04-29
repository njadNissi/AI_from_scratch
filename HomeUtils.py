import os
import sys
import streamlit as st
import io
import contextlib
import pandas as pd
import json
import builtins
import uuid

def build_dynamic_navigation(base_path="pages"):
    nav_dict = {}
    path_map = {}
    
    for root, dirs, files in os.walk(base_path):
        py_files = [f for f in files if f.endswith(".py") and not f.startswith("__")]
        
        if py_files:
            # 1. Determine the Section Name (This creates the tree headers)
            relative_path = os.path.relpath(root, base_path)
            if relative_path == ".":
                section_name = "General"
            else:
                # Converts "linear_regression" to "Linear Regression"
                section_name = relative_path.replace("_", " ").title()
            
            pages_in_section = []
            
            for f in sorted(py_files):
                full_path = os.path.abspath(os.path.join(root, f))
                page_label = f.replace(".py", "").replace("-", " ").replace("_", " ").title()
                
                # 2. FLATTEN the URL Path
                # Replace slashes with dashes so Streamlit doesn't think it's nested
                flat_url = f"{section_name}-{f.replace('.py', '')}".lower().replace(" ", "-").replace("/", "-")
                
                page_obj = st.Page(full_path, title=page_label, url_path=flat_url)
                pages_in_section.append(page_obj)
                
                # Map the flat URL to the actual file path for our code viewer
                path_map[flat_url] = full_path
            
            # 3. Add the list of pages to the specific section key
            nav_dict[section_name] = pages_in_section

    return nav_dict, path_map


class StreamlitRedirector:
    def __init__(self, placeholder, page_key):
        self.placeholder = placeholder
        self.page_key = f"log_{page_key}"
        
        # 1. Initialize session state for this specific page if it doesn't exist
        if self.page_key not in st.session_state:
            st.session_state[self.page_key] = ""
        
        # 2. Start with whatever was previously saved
        self.buffer = st.session_state[self.page_key]
        self._update_ui()

    def write(self, text):
        # 3. Append to both buffer and persistent session state
        self.buffer += text
        st.session_state[self.page_key] = self.buffer
        self._update_ui()

    def _update_ui(self):
        # Your existing Terminal UI logic
        self.placeholder.markdown(
            f"""
            <div id="terminal-box" style="
                height: 400px;
                overflow-y: auto;
                white-space: pre-wrap;
                font-family: monospace;
                background-color: #1e1e1e;
                color: #00ff00;
                padding: 15px;
                border-radius: 5px;
            ">{self.buffer}</div>
            """, 
            unsafe_allow_html=True
        )

    def flush(self):
        pass
    

class PersistentRedirector:
    def __init__(self, placeholder, key):
        self.placeholder = placeholder
        self.key = f"log_{key}"

    def write(self, text):
        # Directly update the session state global memory
        st.session_state[self.key] += text
        self.display()

    def display(self):
        # Always render what is currently in the session state
        content = st.session_state[self.key]
        self.placeholder.markdown(
            f"""
            <div id="terminal-box" style="
                height: 400px; overflow-y: auto; white-space: pre-wrap;
                font-family: monospace; background-color: #1e1e1e;
                color: #00ff00; padding: 15px; border-radius: 5px;
                border: 1px solid #444;
            ">{content}</div>
            """, 
            unsafe_allow_html=True
        )

    def flush(self):
        pass
    
    
def add_code_col(path_map:dict, pg):
    st.subheader("� Source Code")
    # Set a fixed height (e.g., 600 pixels) for the code view
    with st.container(height=600, border=True):
        target_file = path_map.get(pg.url_path)
        if target_file and os.path.exists(target_file):
            with open(target_file, "r", encoding="utf-8") as f:
                st.code(f.read(), language="python")
        else:
            st.info("Select a page to view code.")

            
def add_result_col(path_map:dict, pg):
    st.subheader("🚀 Execution Result")
    my_redirector = None
    
    with st.container(height=600, border=True):
        # 1. Create a horizontal pane for input and the trigger
        col_input, col_btn, col_clr = st.columns([0.7, 0.15, 0.15])
        
        with col_input:
            mock_val = st.text_input(
                "Terminal Input:", 
                key=f"input_{pg.url_path}",
                label_visibility="collapsed", # Cleaner look
                placeholder="Enter input here..."
            )
        
        with col_btn:
            # The button returns True only on the click event
            run_clicked = st.button("▶️ Run", key=f"run_{pg.url_path}", use_container_width=True)
            
        with col_clr:
            if st.button("🧹 Clear", key=f"clear_{pg.url_path}", use_container_width=True):
                # Clear the session state log for this page
                log_key = f"log_{pg.url_path}"
                if log_key in st.session_state:
                    st.session_state[log_key] = ""
        
        st.divider() # Visual separation between controls and output
        
        # 2. Terminal Output Area
        terminal_placeholder = st.empty()
        def run_with_mock():
            global my_redirector
            # 1. Get the directory of the script we are about to run
            current_full_path = path_map.get(pg.url_path)
            script_dir = os.path.dirname(current_full_path)
            
            # 2. Add it to the front of sys.path
            if script_dir not in sys.path:
                sys.path.insert(0, script_dir)

            # 3. Initialize the log for this page in Session State if it doesn't exist
            if f"log_{pg.url_path}" not in st.session_state:
                st.session_state[f"log_{pg.url_path}"] = f"--- Session for {pg.title} initialized ---\n"
            my_redirector = PersistentRedirector(terminal_placeholder, key=pg.url_path)
            my_redirector.display()

            original_input = builtins.input
            builtins.input = lambda _: mock_val
            
            try:
                with contextlib.redirect_stdout(my_redirector):
                    # 3. Use exec() to run the code in its own context
                    # This is often safer than pg.run() for deep sub-scripts
                    with open(current_full_path, "r") as f:
                        code = f.read()
                        exec(code, {"__name__": "__main__", "__file__": current_full_path})
            except Exception as e:
                st.error(f"Execution Error: {e}")
            finally:
                builtins.input = original_input
                # 4. Optional: Clean up sys.path if you want to avoid pollution
                if script_dir in sys.path:
                    sys.path.remove(script_dir)

        # 3. Execution Logic: Only run if the button is clicked
        if run_clicked:
            run_with_mock()
        elif my_redirector is not None:
            my_redirector.display()
        else:
            terminal_placeholder.info("Click 'Run' to execute the script.")


def add_artifacts_panel(target_file):
    if not target_file:
        return

    script_dir = os.path.dirname(target_file)
    artifacts_dir = os.path.join(script_dir, "artifacts")
    
    if os.path.exists(artifacts_dir) and os.path.isdir(artifacts_dir):
        # 1. Define Categories
        media_ext = ('.png', '.jpg', '.jpeg', '.gif', '.mp4', '.mov')
        data_ext = ('.csv', '.json', '.txt')
        model_ext = ('.keras', '.tflite', '.h5', '.pkl', '.pickle', '.pt', '.pth')
        
        all_files = sorted(os.listdir(artifacts_dir))
        
        if all_files:
            st.divider()
            st.subheader("📦 Generated Artifacts")
            
            # Use tabs to keep the UI clean
            tab_media, tab_data, tab_models = st.tabs(["🖼️ Media", "📊 Data", "🧠 Models"])

            with tab_media:
                media_files = [f for f in all_files if f.lower().endswith(media_ext)]
                if media_files:
                    cols = st.columns(2)
                    for idx, f in enumerate(media_files):
                        with cols[idx % 2]:
                            path = os.path.join(artifacts_dir, f)
                            if f.lower().endswith(('.mp4', '.mov')):
                                st.video(path)
                            else:
                                st.image(path, caption=f, use_container_width=True)
                else:
                    st.info("No media artifacts found.")

            with tab_data:
                data_files = [f for f in all_files if f.lower().endswith(data_ext)]
                if data_files:
                    for f in data_files:
                        path = os.path.join(artifacts_dir, f)
                        with st.expander(f"📄 {f}"):
                            # Show download button for data
                            with open(path, "rb") as file_bytes:
                                st.download_button(label=f"Download {f}", data=file_bytes, file_name=f)
                            # Show preview (first 500 chars)
                            if f.endswith(('.txt', '.csv', '.json')):
                                with open(path, "r") as t:
                                    st.text(t.read(500) + "...")
                else:
                    st.info("No data artifacts found.")

            with tab_models:
                model_files = [f for f in all_files if f.lower().endswith(model_ext)]
                if model_files:
                    for f in model_files:
                        path = os.path.join(artifacts_dir, f)
                        # Get file size in MB
                        file_size = os.path.getsize(path) / (1024 * 1024)
                        
                        # Create a "Card" for each model
                        with st.container(border=True):
                            col1, col2 = st.columns([3, 1])
                            col1.markdown(f"**{f}** \n`Size: {file_size:.2f} MB`")
                            
                            # Read file as binary for download
                            with open(path, "rb") as model_file:
                                col2.download_button(
                                    label="💾 Download",
                                    data=model_file,
                                    file_name=f,
                                    key=f"dl_{f}" # Unique key for each button
                                )
                else:
                    st.info("No model files found.")
                    

def add_utilities():
    # 2. Sidebar System Utilities
    with st.sidebar:
        st.divider()
        with st.expander("🛠️ System Utilities"):
            st.write("Use these if hardware (Camera/GPU) gets locked.")
            
            if st.button("🚨 Reset Camera Handle", use_container_width=True):
                # Kills any process holding the camera device
                os.system("sudo fuser -k /dev/video0")
                st.success("Camera handle cleared!")
                
            if st.button("🧹 Clear GPU Memory", use_container_width=True):
                # Clears zombie processes from the GPU
                os.system("nvidia-smi --gpu-reset") # Or your custom PID kill logic
                st.success("GPU memory reset!")                  