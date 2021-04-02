# **Smoothie Shop**

This project will allow customers to order smoothies from a menu or select ingredients on a per cost basis and have them made into a smoothie. It will then
bill the customer and take away from their wallet funds, if no wallet funds then it will say come back later. 

## **The breakdown of this application is as follows**:
- CSV files containing information required for menu, smoothies, fruits, prices and wallet balance. 
- Systems to read those CSV files into program.
- Show the menu to the user through terminal / GUI. 
- Allow user to create order within terminal / GUI.
- Add items to order.
- Review current order
- Amend the order if you decide you want anything else
- View wallet balance. 
- Pay for order.

## **Additional updates to the application may include**:
- Graphical User Interface across all application.
- Custom orders, allowing you to create your own smoothie from ingredients.
- Receipt from order after paying. 
- Transaction history for managers.

The project makes use of adapter design patterns to allow for swapping out the input that is being used within the CustomerOrder class. Our main class is CustomerOrder which has addItems, orderReview, confirmOrder, removeItem and orderTotal methods within the class. This class makes use of InputConsole class, ReadSmoothieFile class and CustomSmoothie class. 
The ReadSmoothieFile class uses the ReadCSVFile class to read our smoothie menu csv file and then return it, which is then accessed by the main CustomerOrder class. 
