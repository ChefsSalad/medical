import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
# 设置页面标题和布局
st.set_page_config(page_title="UKB-DRP Tool", layout="wide")
st.title("Risk group stratifications of dementia and Alzheimer's Disease")
# 左侧面板输入
st.sidebar.title("UKB-DRP Tool")
#col1, col2, col3, col4 = st.sidebar.columns(4)
col1, col2, col3 = st.sidebar.columns([1, 1, 2])
# 第一列的输入
with col1:
    PTEDUCAT= st.slider("PTEDUCAT", 6.0, 20.0)
    Entorhinal = st.slider("Entorhinal", 1270.0, 5902.0)
    EcogSPOrgan = st.slider("EcogSPOrgan", 1.0, 4.0)
    EcogSPVisspat = st.slider("EcogSPVisspat", 1.0, 4.0)
    EcogSPMem = st.slider("EcogSPMem", 1.0, 4.0)
    EcogSPLang= st.slider("EcogSPLang", 1.0, 4.0)
    EcogSPDivatt = st.slider("EcogSPDivatt", 1.0, 4.0)
    EcogPtOrgan= st.slider("EcogPtOrgan", 1.0, 4.0)
    EcogSPTotal = st.slider("EcogSPTotal", 1.0, 4.0)
    EcogPtVisspat = st.slider("EcogPtVisspat", 1.0, 4.0)



# 第二列的输入
with col2:
    ADAS11 = st.slider("ADAS11", 0.0, 70.0)
    MOCA = st.slider("MOCA", 0.0, 30.0)
    FAQ = st.slider("FAQ", 0.0, 30.0)
    CDRSB = st.slider("CDRSB", 0.0, 17.0)
    FDG = st.slider("FDG ", 0.75086, 1.75332)
    DXCHANGE= st.slider("DXCHANGE ", -1.0, 8.0)
    RAVLT_immediate = st.slider("RAVLT_immediate", 0.0, 75.0)
    RAVLT_learning = st.slider("RAVLT_learning", -5.0, 14.0)
    RAVLT_forgetting= st.slider("RAVLT_forgetting", -9.0, 15.0)
    RAVLT_perc_forgetting = st.slider("RAVLT_perc_forgetting", -450.0, 100.0)


with col3:
    MidTemp = st.number_input("MidTemp", 10776.0, 29292.0)
    TAU_UPENNBIOMK9_04_19_17 = st.number_input("TAU_UPENNBIOMK9_04_19_17", 99.79, 811.7)
    PTAU_UPENNBIOMK9_04_19_17 = st.number_input("PTAU_UPENNBIOMK9_04_19_17", 8.21, 82.04)
    ST111TS_UCSFFSX_11_02_15_UCSFFSX51_08_01_16 = st.number_input("ST111TS_UCSFFSX_11_02_15_UCSFFSX51_08_01_16", 0.449,
                                                                  1.073)
    ST6SV_UCSFFSX_11_02_15_UCSFFSX51_08_01_16 = st.number_input("ST6SV_UCSFFSX_11_02_15_UCSFFSX51_08_01_16", 43.0,
                                                                1461.0)
    ST62SA_UCSFFSX_11_02_15_UCSFFSX51_08_01_16 = st.number_input("ST62SA_UCSFFSX_11_02_15_UCSFFSX51_08_01_16", 207.0,
                                                                 888.0)
    ST83TA_UCSFFSX_11_02_15_UCSFFSX51_08_01_16 = st.number_input("ST83TA_UCSFFSX_11_02_15_UCSFFSX51_08_01_16", 1.487,
                                                                 4.534)
    ST44SA_UCSFFSX_11_02_15_UCSFFSX51_08_01_16 = st.number_input("ST44SA_UCSFFSX_11_02_15_UCSFFSX51_08_01_16", 127.0,
                                                                 1189.0)
    marital_status_options = {
        0: "Married",
        1: "Divorced",
        2: "Widowed",
        3: "Never married",
        4: "Unknown"
    }

    # 创建下拉选择框
    selected_status = st.selectbox("PTMARRY", list(marital_status_options.values()))
    APOE4= st.selectbox("APOE4", [0,1,2])
    c= st.selectbox("c", [0,1,2])
    # 获取选中的数值
    PTMARRY= list(marital_status_options.keys())[list(marital_status_options.values()).index(selected_status)]

def plot_risk_chart1(title, observed, predicted):
    deciles = np.arange(1, 11)
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))  # 设置图形宽度
    ax.bar(deciles - width / 2, observed, width, label='Observed', color='orange')
    ax.bar(deciles + width / 2, predicted, width, label='Predicted', color='blue')

    ax.set_xlabel('Decile groups (10% quantile each)')
    ax.set_ylabel('Frequency (%)')
    ax.set_title(title)
    ax.legend()

    return fig

def plot_risk_chart2(title, observed, predicted):
    deciles = np.arange(1, 11)
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 1))  # 设置图形宽度
    ax.bar(deciles - width / 2, observed, width, label='Observed', color='orange')
    ax.bar(deciles + width / 2, predicted, width, label='Predicted', color='blue')

    ax.set_xlabel('Decile groups (10% quantile each)')
    ax.set_ylabel('Frequency (%)')
    ax.set_title(title)
    ax.legend()

    return fig
# 示例数据
observed_mmse = np.random.rand(10) * 100
predicted_mmse = np.random.rand(10) * 100
observed_adas = np.random.rand(10) * 100
predicted_adas = np.random.rand(10) * 100
observed_dx = np.random.rand(10) * 100
predicted_dx = np.random.rand(10) * 100

# 创建两列布局
col1, col2 = st.columns(2)

# MMSE风险图
with col1:
    st.subheader("MMSE Risk Chart")
    mmse_fig = plot_risk_chart1('MMSE Risk Chart', observed_mmse, predicted_mmse)
    st.pyplot(mmse_fig)

# ADAS风险图
with col2:
    st.subheader("ADAS Risk Chart")
    adas_fig = plot_risk_chart1('ADAS Risk Chart', observed_adas, predicted_adas)
    st.pyplot(adas_fig)

# DX风险图
st.subheader("DX Risk Chart")
dx_fig = plot_risk_chart2('DX Risk Chart', observed_dx, predicted_dx)
st.pyplot(dx_fig)

# st.sidebar.write(
#     "The UK Biobank-Dementia Risk Prediction (UKB-DRP) tool was established based on UK Biobank study cohort. The tool was developed on research purpose and cannot be used as clinical evidence.")
