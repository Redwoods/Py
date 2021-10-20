import streamlit as st
st.text("streamlit ver. : " + st.__version__)

# ## Text 
# ## Title
st.title('Streamlit Tutorial: start by pdm00, 이상훈')
# ## Header/Subheader
st.header('This is header')
st.subheader('This is subheader')
# ## Text
st.text("Hello Streamlit! 이 글은 튜토리얼 입니다.")
 
# ## Markdown
st.header('Markdown')
st.markdown('# header-1')
st.markdown('## header-2')
st.markdown('#### header-4')
st.markdown('###### header-6')
 
# # list
st.header('markdown: List')
st.markdown('- list1')
st.markdown('- list2')
st.markdown('- list3\n'
            '   * inner list1\n'
            '   * inner list2\n'
            '       - inner_inner list\n')
 
# # ## Message
st.info("End of first note: **text, markdown**!")
 
## streamlit messages
st.success("Successful")
st.info("Information!")
st.warning("This is a warning")
st.error("This is an error!")
st.exception("NameError('Error name is not defined')")

## Code block
st.header('Code block')
code1 = '''def hello():
    print("Hello, Streamlit!")'''

st.code(code1, language='python')

code2 = '''
def add(a,b):
    return a+b
'''

st.code(code2, language='python')

# ## Latex, raw
st.header('latex')
st.latex(r"\alpha_n, \beta, \gamma, \cdots, \omega")
st.latex(r"Y = \alpha + \beta X_i")
# ## Latex-inline
st.markdown(r"회귀분석에서 오차는 다음과 같습니다 $e_i = y_i - \hat{y}_i$")
# ## Mean squared error
st.subheader("Mean squared error")
st.markdown(r"#### $MSE = \frac{1}{N-1} \sum_{i=1}^{N-1} (y_i - \hat{y}_i)^2$")



