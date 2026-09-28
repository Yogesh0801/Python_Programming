CREATE DATABASE food_ordering;

USE food_ordering;
CREATE TABLE foods (
    food_id INT PRIMARY KEY AUTO_INCREMENT,
    food_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    description VARCHAR(255)
);

INSERT INTO foods
(food_name, category, price, description)
VALUES
('Margherita Pizza', 'Pizza', 249.00, 'Cheese pizza with tomato sauce'),
('Veg Burger', 'Burger', 149.00, 'Veg burger with fresh vegetables'),
('Chicken Biryani', 'Biryani', 199.00, 'Spicy chicken biryani'),
('Masala Dosa', 'South Indian', 120.00, 'Crispy dosa with potato masala'),
('White Sauce Pasta', 'Pasta', 179.00, 'Creamy white sauce pasta');

install flask
pip install flask mysql-connector-python

connect flask with mysql
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="food_ordering"
)



install cloudflared tunnel msi file
check using cloudflared --version
then run
cloudflared tunnel --url http://127.0.0.1:5000