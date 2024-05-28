from flask import Blueprint
from . import db
from .models import Product, ProductDetail, Order
import datetime

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# function to put some seed data in the database
@admin_bp.route('/dbseed')
def dbseed():
    product1 = Product(productname='Polaris GPS Speedometer', price= 119.00, image='row_1_1.jpeg',  product_category='Car GPS', stock_status='Available', product_detail_id=1)

    product2 = Product(productname='Garmin Overlander', price= 1097.00, image='row_1_2.jpeg',  product_category='Car GPS', stock_status='Available', product_detail_id=2)

    product3 = Product(productname='Garmin DriveSmart 66 MT-S', price= 379.00, image='row_1_3.jpeg',  product_category='Car GPS', stock_status='Available', product_detail_id=3)

    product4 = Product(productname='Garmin Drive 53', price= 259.00, image='row_1_4.jpeg',  product_category='Car GPS', stock_status='Available', product_detail_id=4)

    product5 = Product(productname='Garmin Varia RCT715', price= 599.00, image='row_2_1.jpeg',  product_category='Cycling GPS', stock_status='Available', product_detail_id=5)

    product6 = Product(productname='Garmin Varia RTL515', price= 326.00, image='row_2_2.jpeg',  product_category='Cycling GPS', stock_status='Available', product_detail_id=6)

    product7 = Product(productname='Garmin Edge 830', price= 646.00, image='row_2_3.jpeg',  product_category='Cycling GPS', stock_status='Available', product_detail_id=7)

    product8 = Product(productname='Garmin Edge 1030 Plus', price= 864.00, image='row_2_4.jpeg',  product_category='Cycling GPS', stock_status='Available', product_detail_id=8)

    product9 = Product(productname='Garmin Forerunner 55 - Black', price= 299.00, image='row_3_1.jpeg',  product_category='Fitness Watches', stock_status='Available', product_detail_id=9)

    product10 = Product(productname='Garmin tactix 7 Pro Edition', price= 1990.00, image='row_3_2.jpeg',  product_category='Fitness Watches', stock_status='Available', product_detail_id=10)

    product11 = Product(productname='Garmin fenix 7X Sapphire Solar', price= 1439.00, image='row_3_3.jpeg',  product_category='Fitness Watches', stock_status='Available', product_detail_id=11)

    product12 = Product(productname='Garmin tactix 7 Pro Ballistics', price= 1439.00, image='row_3_4.jpeg',  product_category='Fitness Watches', stock_status='Available', product_detail_id=12)

      
    try:
        db.session.add(product1)
        db.session.add(product2)
        db.session.add(product3)
        db.session.add(product4)
        db.session.add(product5)
        db.session.add(product6)
        db.session.add(product7)
        db.session.add(product8)
        db.session.add(product9)
        db.session.add(product10)
        db.session.add(product11)
        db.session.add(product12)
        db.session.commit()
    except:
        return 'There was an issue adding the cities in dbseed function'


    
    product1_detail = ProductDetail(product_description ='''Projects GPS Speed onto the Windscreen Includes audible alerts when approaching a fixed speed or red light camera. This GPS Speed Heads Up Display projects your vehicles speed up onto the windscreen, in your line of sight - in bright, large, green numbers. You can also toggle between the default reflective mode, and the non-reflective mode (similar to the HUD Digital). These easy to read numbers allow you see at a glance what speed you're travelling, without the need to look down at your dashboard. Projects GPS speed onto the windscreen in driver's line of sight, so you don’t have to take your eyes off the road to check your speed. Avoid speeding fines with audible over speed alerts, as well as audible alerts when approaching a fixed speed or red light camera. Max speed 199 km/h. The fixed speed and red-light cameras can be updated annually. The device must be returned to Polaris for this update, and it is $35 (inc. GST).''', product_detail_image='item-2.jpeg', launch_date=datetime.date(2023, 1, 1), bluetooth_support='Yes', language='English', color='Black', made_in ='Australia')

    product2_detail = ProductDetail(product_description ='''Product 2 Speed onto the Windscreen Includes audible alerts when approaching a fixed speed or red light camera. This GPS Speed Heads Up Display projects your vehicles speed up onto the windscreen, in your line of sight - in bright, large, green numbers. You can also toggle between the default reflective mode, and the non-reflective mode (similar to the HUD Digital). These easy to read numbers allow you see at a glance what speed you're travelling, without the need to look down at your dashboard. Projects GPS speed onto the windscreen in driver's line of sight, so you don’t have to take your eyes off the road to check your speed. Avoid speeding fines with audible over speed alerts, as well as audible alerts when approaching a fixed speed or red light camera. Max speed 199 km/h. The fixed speed and red-light cameras can be updated annually. The device must be returned to Polaris for this update, and it is $35 (inc. GST).''', product_detail_image='coming-soon.jpeg', launch_date=datetime.date(2023, 2, 15), bluetooth_support='Yes',language='English',color='Black',made_in='USA')

    product3_detail = ProductDetail(product_description ='''Product 3 Speed onto the Windscreen Includes audible alerts when approaching a fixed speed or red light camera. This GPS Speed Heads Up Display projects your vehicles speed up onto the windscreen, in your line of sight - in bright, large, green numbers. You can also toggle between the default reflective mode, and the non-reflective mode (similar to the HUD Digital). These easy to read numbers allow you see at a glance what speed you're travelling, without the need to look down at your dashboard. Projects GPS speed onto the windscreen in driver's line of sight, so you don’t have to take your eyes off the road to check your speed. Avoid speeding fines with audible over speed alerts, as well as audible alerts when approaching a fixed speed or red light camera. Max speed 199 km/h. The fixed speed and red-light cameras can be updated annually. The device must be returned to Polaris for this update, and it is $35 (inc. GST).''', product_detail_image='coming-soon.jpeg', launch_date=datetime.date(2023, 3, 10), bluetooth_support='Yes', language='English', color='Black', made_in ='Taiwan')

    product4_detail = ProductDetail(product_description ='''Product 4 Speed onto the Windscreen Includes audible alerts when approaching a fixed speed or red light camera. This GPS Speed Heads Up Display projects your vehicles speed up onto the windscreen, in your line of sight - in bright, large, green numbers. You can also toggle between the default reflective mode, and the non-reflective mode (similar to the HUD Digital). These easy to read numbers allow you see at a glance what speed you're travelling, without the need to look down at your dashboard. Projects GPS speed onto the windscreen in driver's line of sight, so you don’t have to take your eyes off the road to check your speed. Avoid speeding fines with audible over speed alerts, as well as audible alerts when approaching a fixed speed or red light camera. Max speed 199 km/h. The fixed speed and red-light cameras can be updated annually. The device must be returned to Polaris for this update, and it is $35 (inc. GST).''', product_detail_image='coming-soon.jpeg', launch_date=datetime.date(2023, 4, 20), bluetooth_support='No', language='English', color='Black', made_in ='Japan')

    product5_detail = ProductDetail(product_description ='''Product 5 Speed onto the Windscreen Includes audible alerts when approaching a fixed speed or red light camera. This GPS Speed Heads Up Display projects your vehicles speed up onto the windscreen, in your line of sight - in bright, large, green numbers. You can also toggle between the default reflective mode, and the non-reflective mode (similar to the HUD Digital). These easy to read numbers allow you see at a glance what speed you're travelling, without the need to look down at your dashboard. Projects GPS speed onto the windscreen in driver's line of sight, so you don’t have to take your eyes off the road to check your speed. Avoid speeding fines with audible over speed alerts, as well as audible alerts when approaching a fixed speed or red light camera. Max speed 199 km/h. The fixed speed and red-light cameras can be updated annually. The device must be returned to Polaris for this update, and it is $35 (inc. GST).''', product_detail_image='coming-soon.jpeg', launch_date=datetime.date(2023, 6, 10), bluetooth_support='Yes', language='English', color='Black', made_in ='Germany')

    product6_detail = ProductDetail(product_description ='''Product 6 Speed onto the Windscreen Includes audible alerts when approaching a fixed speed or red light camera. This GPS Speed Heads Up Display projects your vehicles speed up onto the windscreen, in your line of sight - in bright, large, green numbers. You can also toggle between the default reflective mode, and the non-reflective mode (similar to the HUD Digital). These easy to read numbers allow you see at a glance what speed you're travelling, without the need to look down at your dashboard. Projects GPS speed onto the windscreen in driver's line of sight, so you don’t have to take your eyes off the road to check your speed. Avoid speeding fines with audible over speed alerts, as well as audible alerts when approaching a fixed speed or red light camera. Max speed 199 km/h. The fixed speed and red-light cameras can be updated annually. The device must be returned to Polaris for this update, and it is $35 (inc. GST).''', product_detail_image='coming-soon.jpeg', launch_date=datetime.date(2023, 7, 1), bluetooth_support='Yes', language='English', color='Black', made_in ='USA')

    product7_detail = ProductDetail(product_description ='''Projects GPS Speed onto the Windscreen Includes audible alerts when approaching a fixed speed or red light camera. This GPS Speed Heads Up Display projects your vehicles speed up onto the windscreen, in your line of sight - in bright, large, green numbers. You can also toggle between the default reflective mode, and the non-reflective mode (similar to the HUD Digital). These easy to read numbers allow you see at a glance what speed you're travelling, without the need to look down at your dashboard. Projects GPS speed onto the windscreen in driver's line of sight, so you don’t have to take your eyes off the road to check your speed. Avoid speeding fines with audible over speed alerts, as well as audible alerts when approaching a fixed speed or red light camera. Max speed 199 km/h. The fixed speed and red-light cameras can be updated annually. The device must be returned to Polaris for this update, and it is $35 (inc. GST).''', product_detail_image='coming-soon.jpeg', launch_date=datetime.date(2023, 1, 1), bluetooth_support='Yes', language='English', color='Black', made_in ='Australia')

    product8_detail = ProductDetail(product_description ='''Projects GPS Speed onto the Windscreen Includes audible alerts when approaching a fixed speed or red light camera. This GPS Speed Heads Up Display projects your vehicles speed up onto the windscreen, in your line of sight - in bright, large, green numbers. You can also toggle between the default reflective mode, and the non-reflective mode (similar to the HUD Digital). These easy to read numbers allow you see at a glance what speed you're travelling, without the need to look down at your dashboard. Projects GPS speed onto the windscreen in driver's line of sight, so you don’t have to take your eyes off the road to check your speed. Avoid speeding fines with audible over speed alerts, as well as audible alerts when approaching a fixed speed or red light camera. Max speed 199 km/h. The fixed speed and red-light cameras can be updated annually. The device must be returned to Polaris for this update, and it is $35 (inc. GST).''', product_detail_image='coming-soon.jpeg', launch_date=datetime.date(2023, 1, 1), bluetooth_support='No', language='English', color='Black', made_in ='USA')

    product9_detail = ProductDetail(product_description ='''Projects GPS Speed onto the Windscreen Includes audible alerts when approaching a fixed speed or red light camera. This GPS Speed Heads Up Display projects your vehicles speed up onto the windscreen, in your line of sight - in bright, large, green numbers. You can also toggle between the default reflective mode, and the non-reflective mode (similar to the HUD Digital). These easy to read numbers allow you see at a glance what speed you're travelling, without the need to look down at your dashboard. Projects GPS speed onto the windscreen in driver's line of sight, so you don’t have to take your eyes off the road to check your speed. Avoid speeding fines with audible over speed alerts, as well as audible alerts when approaching a fixed speed or red light camera. Max speed 199 km/h. The fixed speed and red-light cameras can be updated annually. The device must be returned to Polaris for this update, and it is $35 (inc. GST).''', product_detail_image='coming-soon.jpeg', launch_date=datetime.date(2023, 1, 1), bluetooth_support='Yes', language='English', color='Black', made_in ='Germany')

    product10_detail = ProductDetail(product_description ='''Projects GPS Speed onto the Windscreen Includes audible alerts when approaching a fixed speed or red light camera. This GPS Speed Heads Up Display projects your vehicles speed up onto the windscreen, in your line of sight - in bright, large, green numbers. You can also toggle between the default reflective mode, and the non-reflective mode (similar to the HUD Digital). These easy to read numbers allow you see at a glance what speed you're travelling, without the need to look down at your dashboard. Projects GPS speed onto the windscreen in driver's line of sight, so you don’t have to take your eyes off the road to check your speed. Avoid speeding fines with audible over speed alerts, as well as audible alerts when approaching a fixed speed or red light camera. Max speed 199 km/h. The fixed speed and red-light cameras can be updated annually. The device must be returned to Polaris for this update, and it is $35 (inc. GST).''', product_detail_image='coming-soon.jpeg', launch_date=datetime.date(2023, 1, 1), bluetooth_support='No', language='English', color='Black', made_in ='USA')

    product11_detail = ProductDetail(product_description ='''Projects GPS Speed onto the Windscreen Includes audible alerts when approaching a fixed speed or red light camera. This GPS Speed Heads Up Display projects your vehicles speed up onto the windscreen, in your line of sight - in bright, large, green numbers. You can also toggle between the default reflective mode, and the non-reflective mode (similar to the HUD Digital). These easy to read numbers allow you see at a glance what speed you're travelling, without the need to look down at your dashboard. Projects GPS speed onto the windscreen in driver's line of sight, so you don’t have to take your eyes off the road to check your speed. Avoid speeding fines with audible over speed alerts, as well as audible alerts when approaching a fixed speed or red light camera. Max speed 199 km/h. The fixed speed and red-light cameras can be updated annually. The device must be returned to Polaris for this update, and it is $35 (inc. GST).''', product_detail_image='coming-soon.jpeg', launch_date=datetime.date(2023, 1, 1), bluetooth_support='No', language='English', color='Black', made_in ='Germany')

    product12_detail = ProductDetail(product_description ='''Projects GPS Speed onto the Windscreen Includes audible alerts when approaching a fixed speed or red light camera. This GPS Speed Heads Up Display projects your vehicles speed up onto the windscreen, in your line of sight - in bright, large, green numbers. You can also toggle between the default reflective mode, and the non-reflective mode (similar to the HUD Digital). These easy to read numbers allow you see at a glance what speed you're travelling, without the need to look down at your dashboard. Projects GPS speed onto the windscreen in driver's line of sight, so you don’t have to take your eyes off the road to check your speed. Avoid speeding fines with audible over speed alerts, as well as audible alerts when approaching a fixed speed or red light camera. Max speed 199 km/h. The fixed speed and red-light cameras can be updated annually. The device must be returned to Polaris for this update, and it is $35 (inc. GST).''', product_detail_image='coming-soon.jpeg', launch_date=datetime.date(2023, 1, 1), bluetooth_support='Yes', language='English', color='Black', made_in ='Germany')

    try:
        db.session.add(product1_detail)
        db.session.add(product2_detail)
        db.session.add(product3_detail)
        db.session.add(product4_detail)
        db.session.add(product5_detail)
        db.session.add(product6_detail)
        db.session.add(product7_detail)
        db.session.add(product8_detail)
        db.session.add(product9_detail)
        db.session.add(product10_detail)
        db.session.add(product11_detail)
        db.session.add(product12_detail)

        db.session.commit()
    except:
        return 'There was an issue adding the cities in dbseed function'

    return 'DATA LOADED'
