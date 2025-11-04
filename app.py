import os
import platform
import time
import streamlit as st
import psutil

# --- Page Configuration ---
st.set_page_config(page_title="System Monitor", page_icon="🖥️", layout="wide")

# --- Title and Description ---
st.title("🖥️ System Monitor Dashboard")
st.markdown("##### Monitor your system’s performance and configuration in real-time")

# --- System Information Section ---
st.subheader("🔧 System Information")

col1, col2 = st.columns(2)
with col1:
    st.write(f"**OS Type:** {os.name}")
    st.write(f"**System:** {platform.system()}")
    st.write(f"**Release:** {platform.release()}")
    st.write(f"**Processor:** {platform.processor()}")

with col2:
    st.write(f"**Node Name:** {platform.node()}")
    st.write(f"**Version:** {platform.version()}")
    st.write(f"**Current Directory:** `{os.getcwd()}`")
    st.write(f"**Files in Current Directory:** {len(os.listdir())}")

# --- System Performance Section ---
st.subheader("⚙️ Performance Metrics")

# Using psutil for live resource usage
cpu_percent = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')
uptime = time.time() - psutil.boot_time()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="🧠 CPU Usage", value=f"{cpu_percent}%")

with col2:
    st.metric(label="💾 Memory Usage", value=f"{memory.percent}%")

with col3:
    st.metric(label="📀 Disk Usage", value=f"{disk.percent}%")

# --- Progress Bars for Visuals ---
st.subheader("📊 Resource Utilization")

st.progress(int(cpu_percent))
st.progress(int(memory.percent))
st.progress(int(disk.percent))

# --- Live Updating Section ---
st.subheader("⏱️ Uptime Tracker")

st.write(f"**Uptime:** {round(uptime / 3600, 2)} hours since last boot")

# --- Footer ---
st.markdown("---")
st.markdown("Created using **Python** and **Streamlit** by *Prerana Sangole*")

