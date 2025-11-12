Travel Aggregator Analysis – MyNextBooking
Overview

This project analyzes and visualizes data from MyNextBooking, a new Indian travel startup functioning as a travel price aggregator. The platform collects flight and hotel price data from top travel sites like Yatra, MakeMyTrip (MMT), and Goibibo, enabling users to compare prices and find the best deals.

Role: Data Analyst – performed in-depth exploration and visualization of platform data.

Data Sources

Bookings.csv – Contains booking details

Sessions.csv – Contains user interaction and search session data

Workflow & Functioning
1. Data Loading & Cleaning

Imported CSV files using Pandas

Checked data types, missing values, and duplicates

Cleaned columns for consistent structure and correct datatypes

Ensured all IDs (booking_id, session_id, search_id) aligned between datasets

2. Data Analysis

Task 1: Counting Distinct Entities

Counted unique bookings, sessions, and searches

Estimated platform usage and engagement metrics

Task 2: Session Analysis

Analyzed average session duration, number of searches per session, and conversion rate (sessions leading to bookings)

Identified peak activity hours and user behavior trends

Task 3: Platform Comparison

Compared booking frequency and average ticket price across Yatra, MMT, and Goibibo

Determined which platform offers the most competitive pricing

Task 4: Price Trends

Visualized trends using Matplotlib and Seaborn:

Average prices per platform

Booking counts by destination

Seasonal trends (peak travel months/weeks)

Task 5: Correlation & Insights

Checked relationships between user activity (sessions/searches) and actual bookings

Analyzed if more searches lead to better deals or if price sensitivity differs by platform

Libraries & Tools

Pandas: Data loading, cleaning, manipulation

NumPy: Numerical computations

Matplotlib / Seaborn: Trend visualization

Jupyter Notebook: Code execution and presentation
