import streamlit as st
import datetime
import pickle
from sklearn.preprocessing import StandardScaler

st.title(':blue[_Copper_]')
st.caption('Industrial Copper Modeling')
tab1, tab2, tab3 = st.tabs(["Price_Prediction", "Order Status", "About"])

with tab1:
  st.subheader(':blue[_Selling_Price_Finder_]')
  st.subheader(':blue[_Enter the Details_]')

  x=[]
  with st.form("Details1"):
      quantity = st.text_input('Quantity')
      item = st.selectbox('Item Type',('W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR'))
      country = st.selectbox('Country Code',(28, 25, 30, 32, 38, 78, 27, 77, 113, 79, 26, 39, 40, 84, 80, 107, 89))
      application = st.selectbox('Application Type',(10, 41, 28, 59, 15, 4, 38, 56, 42, 26, 27, 19, 20, 66, 
                                                     29, 22, 40, 25, 67, 79, 3, 99, 2, 5,39, 69, 70, 65, 58, 68))
      thickness = st.text_input('Thickness')
      width = st.text_input('Width')
      product = st.selectbox('Product Reference',(1670798778, 1668701718, 628377, 640665, 611993, 1668701376,
                                           164141591, 1671863738, 1332077137,     640405, 1693867550, 1665572374,
                                           1282007633, 1668701698, 628117, 1690738206, 628112, 640400,
                                           1671876026, 164336407, 164337175, 1668701725, 1665572032, 611728,
                                           1721130331, 1693867563, 611733, 1690738219, 1722207579, 929423819,
                                           1665584320, 1665584662, 1665584642))
      order_date = st.date_input("Order Date",datetime.date(2022, 1, 1))
      delivery_date = st.date_input("Estimated Delivery Date",datetime.date(2022, 12, 1))
      submit_button = st.form_submit_button(label="Price")
  k1=['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']
  v1=[5, 6, 3, 1, 2, 0, 4]
  k2=[28, 25, 30, 32, 38, 78, 27, 77, 113, 79, 26, 39, 40, 84, 80, 107, 89]
  v2=[3, 0, 4, 5, 6, 10,  2, 9, 16, 11, 1, 7, 8, 13, 12, 15, 14]
  k3=[10, 41, 28, 59, 15, 4, 38, 56, 42, 26, 27, 19, 20, 66, 29, 22, 40, 25, 67, 79, 3, 99, 2, 5,
      39, 69, 70, 65, 58, 68]
  v3=[4, 17, 12, 21, 5, 2, 14, 19, 18, 10, 11, 6, 7, 23, 13,  8, 16,  9, 24, 28, 1, 29, 0, 3,
      15, 26, 27, 22, 20, 25]
  k4=[1670798778, 1668701718, 628377, 640665, 611993, 1668701376,
      164141591, 1671863738, 1332077137,     640405, 1693867550, 1665572374,
      1282007633, 1668701698, 628117, 1690738206, 628112, 640400,
      1671876026, 164336407, 164337175, 1668701725, 1665572032, 611728,
      1721130331, 1693867563, 611733, 1690738219, 1722207579, 929423819,
      1665584320, 1665584662, 1665584642]
  v4=[24, 22, 5, 8, 2, 20 , 9, 25, 14, 7, 29, 16, 13, 21, 4, 27, 3, 6, 26, 10, 11, 23, 15, 0,
      31, 30, 1, 28, 32, 12, 17, 19, 18]
  if submit_button:
    x.append(float(quantity))
    for i in range(0,len(k1)):
      if item==k1[i]:
        item_type=v1[i]
    x.append(int(item_type))

    for i in range(0,len(k2)):
      if country==k2[i]:
        country_code=v2[i]
    x.append(int(country_code))
      
    for i in range(0,len(k3)):
      if application==k3[i]:
        application_type=v3[i]
    x.append(int(application_type))

    x.append(float(thickness))
    x.append(float(width))

    for i in range(0,len(k4)):
      if product==k4[i]:
        product_ref=v4[i]
    x.append(int(product_ref))
    
    date_1 = datetime.datetime.strptime(str(order_date), "%Y-%m-%d")
    end_date = datetime.datetime.strptime(str(delivery_date), "%Y-%m-%d")
    day=  end_date - date_1
    x.append(day.days)
    # fit scaler on training data
    pickled_scaling = pickle.load(open('scaling_regression.pkl', 'rb'))
    x_=pickled_scaling.transform([x])

    #loading a trained model from pickle file
    pickled_model = pickle.load(open('regression.pkl', 'rb'))
    pred=pickled_model.predict(x_)
    if pred!=None:
      st.info(pred[0])

with tab2:
  st.subheader(':blue[_Order_Status_Finder_]')
  st.subheader(':blue[_Enter the Details_]')

  with st.form("Details2"):
      quantity = st.text_input('Quantity')
      item = st.selectbox('Item Type',('W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR'))
      country = st.selectbox('Country Code',(28, 25, 30, 32, 38, 78, 27, 77, 113, 79, 26, 39, 40, 84, 80, 107, 89))
      application = st.selectbox('Application Type',(10, 41, 28, 59, 15, 4, 38, 56, 42, 26, 27, 19, 20, 66, 
                                                     29, 22, 40, 25, 67, 79, 3, 99, 2, 5,39, 69, 70, 65, 58, 68))
      thickness = st.text_input('Thickness')
      width = st.text_input('Width')
      product = st.selectbox('Product Reference',(1670798778, 1668701718, 628377, 640665, 611993, 1668701376,
                                           164141591, 1671863738, 1332077137,     640405, 1693867550, 1665572374,
                                           1282007633, 1668701698, 628117, 1690738206, 628112, 640400,
                                           1671876026, 164336407, 164337175, 1668701725, 1665572032, 611728,
                                           1721130331, 1693867563, 611733, 1690738219, 1722207579, 929423819,
                                           1665584320, 1665584662, 1665584642))
      selling_price = st.text_input('Price')
      order_date = st.date_input("Order Date",datetime.date(2022, 1, 1))
      delivery_date = st.date_input("Estimated Delivery Date",datetime.date(2022, 1, 1))
      submit_button = st.form_submit_button(label="Status")
  k1=['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']
  v1=[5, 6, 3, 1, 2, 0, 4]
  k2=[28, 25, 30, 32, 38, 78, 27, 77, 113, 79, 26, 39, 40, 84, 80, 107, 89]
  v2=[3, 0, 4, 5, 6, 10,  2, 9, 16, 11, 1, 7, 8, 13, 12, 15, 14]
  k3=[10, 41, 28, 59, 15, 4, 38, 56, 42, 26, 27, 19, 20, 66, 29, 22, 40, 25, 67, 79, 3, 99, 2, 5,
      39, 69, 70, 65, 58, 68]
  v3=[4, 17, 12, 21, 5, 2, 14, 19, 18, 10, 11, 6, 7, 23, 13,  8, 16,  9, 24, 28, 1, 29, 0, 3,
      15, 26, 27, 22, 20, 25]
  k4=[1670798778, 1668701718, 628377, 640665, 611993, 1668701376,
      164141591, 1671863738, 1332077137,     640405, 1693867550, 1665572374,
      1282007633, 1668701698, 628117, 1690738206, 628112, 640400,
      1671876026, 164336407, 164337175, 1668701725, 1665572032, 611728,
      1721130331, 1693867563, 611733, 1690738219, 1722207579, 929423819,
      1665584320, 1665584662, 1665584642]
  v4=[24, 22, 5, 8, 2, 20 , 9, 25, 14, 7, 29, 16, 13, 21, 4, 27, 3, 6, 26, 10, 11, 23, 15, 0,
      31, 30, 1, 28, 32, 12, 17, 19, 18]
  if submit_button:
    x.append(float(quantity))
    for i in range(0,len(k1)):
      if item==k1[i]:
        item_type=v1[i]
    x.append(int(item_type))

    for i in range(0,len(k2)):
      if country==k2[i]:
        country_code=v2[i]
    x.append(int(country_code))
      
    for i in range(0,len(k3)):
      if application==k3[i]:
        application_type=v3[i]
    x.append(int(application_type))

    x.append(float(thickness))
    x.append(float(width))

    for i in range(0,len(k4)):
      if product==k4[i]:
        product_ref=v4[i]
    x.append(int(product_ref))

    x.append(float(selling_price))
    
    date_1 = datetime.datetime.strptime(str(order_date), "%Y-%m-%d")
    end_date = datetime.datetime.strptime(str(delivery_date), "%Y-%m-%d")
    day=  end_date - date_1
    x.append(day.days)

    # fit scaler on training data
    pickled_scaling = pickle.load(open('scaling_Classification.pkl', 'rb'))
    x_=pickled_scaling.transform([x])

    #loading a trained model from pickle file
    pickled_model = pickle.load(open('classification.pkl', 'rb'))
    pred=pickled_model.predict(x_)
    if pred[0]==1:
      st.info('Won')
    elif pred[0]==0:
      st.info('Lost')

with tab3:
  st.subheader(':blue[_How to use:_]')
  st.write('1. Fill the details')
  st.write('2. submit with price/status button')
  st.write('3. you can get the predicted value')
  st.subheader(':blue[_Packages used:_]')
  st.write('Pandas, streamlit, sklearn, pickle')
  st.subheader(':blue[_Demo video:_]')
  st.write('')
  st.subheader(':blue[_GitHub link:_]')
  st.write('https://github.com/kalinharikumar/Industrial-Copper-Modeling.git')