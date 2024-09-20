import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
# 设置页面标题和布局
st.set_page_config(page_title="UKB-DRP Tool", layout="wide")

# 左侧面板输入
st.sidebar.title("UKB-DRP Tool")
#col1, col2, col3, col4 = st.sidebar.columns(4)
col1, col2, col3 = st.sidebar.columns([1, 1, 2])
# 第一列的输入
with col1:
    ADAS11 = st.slider("ADAS11", 0.0, 70.0)
    MOCA = st.slider("MOCA", 0.0, 30.0)
    FAQ = st.slider("FAQ", 0.0, 30.0)
    CDRSB = st.slider("CDRSB", 0.0, 17.0)
    FDG = st.slider("FDG ", 0.75086, 1.75332)
    RAVLT_immediate = st.slider("RAVLT_immediate", 0.0, 75.0)
    RAVLT_learning = st.slider("RAVLT_learning", -5.0, 14.0)
    RAVLT_forgetting= st.slider("RAVLT_forgetting", -9.0, 15.0)
    RAVLT_perc_forgetting = st.slider("RAVLT_perc_forgetting", -450.0, 100.0)


# 第二列的输入
with col2:
    Entorhinal = st.slider("Entorhinal", 1270.0, 5902.0)
    EcogSPOrgan = st.slider("EcogSPOrgan", 1.0, 4.0)
    EcogSPVisspat = st.slider("EcogSPVisspat", 1.0, 4.0)
    EcogSPMem = st.slider("EcogSPMem", 1.0, 4.0)
    EcogSPLang= st.slider("EcogSPLang", 1.0, 4.0)
    EcogSPDivatt = st.slider("EcogSPDivatt", 1.0, 4.0)
    EcogPtOrgan= st.slider("EcogPtOrgan", 1.0, 4.0)
    EcogSPTotal = st.slider("EcogSPTotal", 1.0, 4.0)
    EcogPtVisspat = st.slider("EcogPtVisspat", 1.0, 4.0)


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

# 生成图表
# 生成图表函数
def plot_risk_chart(title, observed, predicted):
    deciles = np.arange(1, 11)
    fig, ax = plt.subplots(figsize=(5, 3))
    width = 0.35

    ax.bar(deciles - width / 2, observed, width, label='Observed', color='orange')
    ax.bar(deciles + width / 2, predicted, width, label='Predicted', color='blue')

    ax.set_xlabel('Decile groups (10% quantile each)')
    ax.set_ylabel('Frequency (%)')
    ax.set_title(title)
    ax.legend()

    return fig

# 显示标题
st.title("Risk group stratifications of dementia and Alzheimer's Disease")

# 创建两列
col1, col2 = st.columns(2)

# 在第一列中显示 "Dementia" 风险图
with col1:
    st.subheader("Risk group stratifications of dementia")
    fig1 = plot_risk_chart("The risk to become dementia",
                           [0.29, 0.3, 0.16, 0.56, 0.47, 1.48, 1.65, 2.39, 2.9, 57.7],
                           [0.29, 0.3, 0.16, 0.56, 0.47, 1.48, 1.65, 2.39, 2.9, 57.6])
    st.pyplot(fig1)

# 在第二列中显示 "Alzheimer's Disease" 风险图
with col2:
    st.subheader("Risk group stratifications of Alzheimer's Disease")
    fig2 = plot_risk_chart("The risk to become Alzheimer's",
                           [0.21, 0.16, 0.15, 0.42, 0.55, 0.91, 1.44, 3.19, 8.95, 28.6],
                           [0.21, 0.16, 0.15, 0.42, 0.55, 0.91, 1.44, 3.19, 8.95, 28])
    st.pyplot(fig2)

predicted_results = {
    "DXCHANGE": 8,
    "PTEDUCAT": 20,
    "PTMARRY": 0.368421053,
    "APOE4": 0,
    "c": 1
}
st.title("预测结果展示")

# 将预测结果转换为表格形式
df = pd.DataFrame(list(predicted_results.items()), columns=["CONDITION", "Predicted Value"])
# 显示预测结果表格
st.table(df)
st.sidebar.write(
    "The UK Biobank-Dementia Risk Prediction (UKB-DRP) tool was established based on UK Biobank study cohort. The tool was developed on research purpose and cannot be used as clinical evidence.")
