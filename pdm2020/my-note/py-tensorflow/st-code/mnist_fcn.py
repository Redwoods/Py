#
# Streamlit webapp : mnist_fcn.py
#
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import tensorflow.keras.backend as K

tf.keras.backend.clear_session()  # For memory

st.set_option('deprecation.showPyplotGlobalUse', False)

mnist = tf.keras.datasets.mnist

# GPU check (Ndivia GPU)
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        st.write("#### ", len(gpus), "Physical GPUs,",
                 len(logical_gpus), "Logical GPUs")
    except RuntimeError as e:
        # Memory growth must be set before GPUs have been initialized
        st.write(e)
else:
    st.write('#### No CUDA supported GPU in this computer.')

# Sidebar setting
# Set some elements which will be useful during training.
st.sidebar.header('Fit model : ')
st.sidebar.subheader('하이퍼 파라미터를 선택하세요.')
batch_size = st.sidebar.selectbox('batch_size를 선택하세요.', [32, 64, 128, 256])
epochs = st.sidebar.selectbox('epochs횟수를 선택하세요.', [10, 20, 50, 100])
loss_function = st.sidebar.selectbox('Loss function', [
                                     'mean_squared_error', 'mean_absolute_error', 'categorical_crossentropy'])
optimizer = st.sidebar.selectbox('Optimizer', ['SGD', 'RMSprop', 'Adam'])
st.sidebar.subheader('모델의 성능')

# FCN
st.title('FCN(완전연결신경망)')
st.write('Fully Connected Neural Networks')
st.header('Dataset: **mnist**')
# spending a few lines to describe our dataset
st.subheader("mnist란?")
st.markdown("1. 데이터 구조\n"
            "   - MNIST 데이터란 필기 숫자의 분류를 위한 학습 데이터 집합\n"
            "   - 28x28 이미지는 화소값이 0 ~ 255인 그레이 이미지\n"
            "   - 0 부터 9 까지의 숫자를 28x28 픽셀 크기의 이미지로 구성\n"
            "   - 1개의 레코드(1개의행 row)는 785개의 숫자로 구성")
st.markdown("2. 트레인/테스트 데이터\n"
            "   - 트레인 데이터: 60000\n"
            "   - 테스트 데이터: 10000")

# Load and divide data into training and test set
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# Normalization of data: [0 ~ 255] => [0.0 ~ 1.0]
X_train = X_train/255.0
X_test = X_test/255.0

# One-hot encoding
y_test1 = tf.keras.utils.to_categorical(y_test, 10)
y_train1 = tf.keras.utils.to_categorical(y_train, 10)

if st.checkbox('Show images sizes'):
    st.write(f'##### X Train Shape: {X_train.shape}')
    st.write(f'##### X Test Shape: {X_test.shape}')
    st.write(f'##### Y Train Shape: {y_train.shape}')
    st.write(f'##### Y Test Shape: {y_test.shape}')


# display one random image from our training set:
class_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
st.subheader('Visualizing dataset')
if st.checkbox('Show random image from the train set'):
    num = np.random.randint(0, X_train.shape[0])
    image = X_train[num]
    # , use_column_width=False)
    st.image(image, caption=class_names[y_train[num]], width=96)

if st.checkbox('Show 10 different image from the train set'):
    num_10 = np.unique(y_train, return_index=True)[1]
#     st.write(num_10)
    images = X_train[num_10]
    plt.figure(figsize=(5, 3))
    for i in range(len(images)):
        # define subplot
        plt.subplot(2, 5, 1 + i)  # , sharey=False)
        # plot raw pixel data
        plt.imshow(images[i])
        plt.title(class_names[i])
        plt.xticks([])
        plt.yticks([])
    plt.suptitle("10 different numbers", fontsize=18)
    st.pyplot()


# Build FCN
st.subheader('FCN 모델 만들기')

# Initialize model
model = tf.keras.Sequential()
# Flattening to make an input(768,) to FCN
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))

# FCN - Dense layers
st.subheader('FCN Layers (최대 5층)')
if st.checkbox('첫번째 은닉층(hidden layer)에 적용할 활성화함수와, 노드의 갯수를 선택하세요.', key='cb1'):
    fcn1 = st.selectbox(
        "노드의 갯수 :", [32, 64, 128, 256, 512], key="<uniquevalueofsomesort>")
    act1 = st.selectbox(
        "활성화 함수 목록 :", ['relu',  'tanh', 'sigmoid'], key="<uniquevalueofsomesort>")
    model.add(tf.keras.layers.Dense(fcn1, activation=act1))
    if st.checkbox('첫번째 은닉층에 dropout를 설정 하시겠습니까?', key='cb11'):
        drop1 = st.selectbox('dropout 비율을 선택해주세요.', [
                             0.0, 0.1, 0.25, 0.5], key="<uniquevalueofsomesort>")
        model.add(tf.keras.layers.Dropout(drop1))
        st.success(
            "#### FCN-1 (filters={0},activation= {1},dropout= {2}))".format(fcn1, act1, drop1))


if st.checkbox('두번째 은닉층(hidden layer)에 적용할 활성화함수와, 노드의 갯수를 선택하세요.', key='cb2'):
    fcn2 = st.selectbox(
        "노드의 갯수 :", [32, 64, 128, 256, 512], key="<uniquevalueofsomesort2>")
    act2 = st.selectbox(
        "활성화 함수 목록 :", ['relu',  'tanh', 'sigmoid'], key="<uniquevalueofsomesort2>")
    model.add(tf.keras.layers.Dense(fcn2, activation=act2))
    if st.checkbox('두번째 은닉층에 dropout를 설정 하시겠습니까?', key='cb21'):
        drop2 = st.selectbox('dropout 비율을 선택해주세요.', [
                             0.0, 0.1, 0.25, 0.5], key="<uniquevalueofsomesort2>")
        model.add(tf.keras.layers.Dropout(drop2))
        st.success(
            "#### FCN-2 (filters={0},activation= {1},dropout= {2}))".format(fcn2, act2, drop2))

if st.checkbox('세번째 은닉층(hidden layer)에 적용할 활성화함수와, 노드의 갯수를 선택하세요.', key='cb3'):
    fcn3 = st.selectbox(
        "노드의 갯수 :", [32, 64, 128, 256, 512], key="<uniquevalueofsomesort3>")
    act3 = st.selectbox(
        "활성화 함수 목록 :", ['relu',  'tanh', 'sigmoid'], key="<uniquevalueofsomesort3>")
    model.add(tf.keras.layers.Dense(fcn3, activation=act3))
    if st.checkbox('세번째 은닉층에 dropout를 설정 하시겠습니까?', key='cb31'):
        drop3 = st.selectbox('dropout 비율을 선택해주세요.', [
                             0.0, 0.1, 0.25, 0.5], key="<uniquevalueofsomesort3>")
        model.add(tf.keras.layers.Dropout(drop3))
        st.success(
            "#### FCN-3 (filters={0},activation= {1},dropout= {2}))".format(fcn3, act3, drop3))

if st.checkbox('네번째 은닉층(hidden layer)에 적용할 활성화함수와, 노드의 갯수를 선택하세요.', key='cb4'):
    fcn4 = st.selectbox(
        "노드의 갯수 :", [32, 64, 128, 256, 512], key="<uniquevalueofsomesort4>")
    act4 = st.selectbox(
        "활성화 함수 목록 :", ['relu',  'tanh', 'sigmoid'], key="<uniquevalueofsomesort4>")
    model.add(tf.keras.layers.Dense(fcn4, activation=act4))
    if st.checkbox('네번째 은닉층에 dropout를 설정 하시겠습니까?', key='cb41'):
        drop4 = st.selectbox('dropout 비율을 선택해주세요.', [
                             0.0, 0.1, 0.25, 0.5], key="<uniquevalueofsomesort4>")
        model.add(tf.keras.layers.Dropout(drop4))
        st.success(
            "#### FCN-4 (filters={0},activation= {1},dropout= {2}))".format(fcn4, act4, drop4))

# output layer - 'softmax'
st.subheader('Check the below box to complete your model!')
if st.checkbox('Add output layer.', key='cb5'):
    model.add(tf.keras.layers.Dense(10, activation='softmax'))
    st.success("#### Output (filters=10,activation= 'softmax')")
    st.info('Model was successfully constructed!')

# Compile the model
model.compile(loss=loss_function, optimizer=optimizer, metrics=['accuracy'])

# Summary of model
if st.checkbox('모델의 구조를 확인.'):
    # st.write(model)
    st.write('name, output_shape, parameters')
    for layer in model.layers:
        st.write(type(layer), layer.output_shape, layer.count_params())

#        
# function to fit the model (using cache)
@st.cache(suppress_st_warning=True)
def fit_model(fit_flag="all"):
    if(fit_flag=="all"):
        history = model.fit(X_train, y_train1,
                        batch_size=batch_size,
                        shuffle=True,
                        epochs=epochs,
                        validation_data=(X_test, y_test1))
    else:
        history = model.fit(X_train[:1000], y_train1[:1000],
                        batch_size=batch_size,
                        shuffle=True,
                        epochs=epochs,
                        validation_data=(X_test[0:1000], y_test1[0:1000]))

    # Plot training & validation accuracy values
    acc_list = [100 * i for i in history.history['accuracy']]
    vacc_list = [100 * i for i in history.history['val_accuracy']]
    plt.plot(range(1, epochs+1), acc_list)  # history.history['accuracy'])
    plt.plot(range(1, epochs+1), vacc_list)  # history.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy (%)')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    st.pyplot()

    predictions = model.predict(X_test)  # X_test/ 255.0)
    scores = model.evaluate(X_test, y_test1)

    tf.keras.backend.clear_session()  # For memory

    return predictions, scores


st.subheader('Fit model')
fit_len = st.selectbox(
        "학습에 이용할 데이터 수는?", ["1000","all"], key="<uniquevalueofsomesort4>")
st.text("Please clear cache to train new model")
if st.checkbox('모델 학습'):
    predictions, scores = fit_model(fit_len)

    st.sidebar.markdown('**Current model**')
    st.sidebar.markdown(f'loss: {round(scores[0],2)}')
    st.sidebar.markdown(f'accuracy: {round(100*scores[1],2)}%')
    # print("scores[1]",scores[1])
#     st.sidebar.markdown('**Best model**')

model_best = keras.models.load_model('./model/fcn3_best.hdf5') 
predictions_best=model_best.predict(X_test) 
scores_best = model_best.evaluate(X_test, y_test1)
st.sidebar.markdown('**Best model**')   
st.sidebar.markdown(f'- loss: {round(scores_best[0],2)}')   
st.sidebar.markdown(f'- accuracy: {round(100*scores_best[1],2)}%')


##########################################
# Visualizing results
##########################################
st.subheader('Visualizing results: mnist')


def plot_pred(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array[i], true_label[i:i+1], img[i]
    plt.grid(False)
    plt.title(class_names[true_label[0]])
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:   # np.argmax(true_label)
        st.success("Test image-%d: Classified correctly" % i)
    else:
        st.error("Test image-%d: Wrong classification" % i)


def plot_bar(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array[i], true_label[i]
    plt.grid(False)
    plt.yticks([])
    plt.xticks(np.arange(10), class_names, rotation=0)

    thisplot = plt.bar(range(10), predictions_array, color='grey')
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    if predicted_label == true_label:  # np.argmax(true_label):
        color = 'green'
    else:
        color = 'red'

    thisplot[predicted_label].set_color(color)


# Show random prediction results
# if st.checkbox('Show random prediction results'):
#     num2 = np.random.randint(0, len(y_test[:1000]))
#     plt.figure(figsize=(9, 4))
#     plt.subplot(1, 2, 1)
#     plot_pred(num2, predictions, y_test, X_test)
#     plt.subplot(1, 2, 2)
#     plot_bar(num2, predictions,  y_test)
#     plt.title("Green: True, Red: False")
#     st.pyplot()
if st.checkbox('Show random prediction results, and compare with best model'):
    np.random.seed(None)
    num = np.random.randint(0, len(y_test))
#     st.write("## ", num2)
    plt.figure(figsize=(5,4))
    plt.subplot(2,2,(1,2))
    plot_pred(num, predictions, y_test, X_test)
    plt.subplot(2,2,3)
    plot_bar(num, predictions,  y_test)
    plt.title("Green: True, Red: False")
    plt.subplot(2,2,4)
    plot_bar(num, predictions_best,  y_test)
    plt.title("The best model")
    st.pyplot()
