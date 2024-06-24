# 🏛️ Museum Data Analysis Project

This project involves the analysis of museum data using PostgreSQL. The dataset includes information about artists, canvas sizes, images, museums, museum hours, product sizes, subjects, and works. The goal of the project is to perform various queries to derive insights and answer specific questions related to the museum data.

## 📊 Dataset Overview

The dataset comprises the following tables:

- **🎨 artist**: Information about artists.
- **🖼️ canvas_size**: Details of canvas sizes.
- **🔗 image_link**: Links to images.
- **🏛️ museum**: Information about museums.
- **🕰️ museum_hours**: Museum opening hours.
- **📏 product_size**: Product sizes and pricing details.
- **📚 subject**: Subjects of artworks.
- **🖌️ work**: Details of artworks.

## 🎯 Project Objectives

The project aims to address several questions and problems related to the museum data, including:

1. Fetching all paintings not displayed in any museum.
2. Identifying museums without any paintings.
3. Finding paintings with asking prices higher than their regular prices.
4. Identifying paintings with asking prices less than 50% of their regular prices.
5. Determining the most expensive canvas size.
6. Deleting duplicate records from multiple tables.
7. Identifying museums with invalid city information.
8. Removing invalid entries in the `museum_hours` table.
9. Fetching the top 10 most famous painting subjects.
10. Identifying museums open on both Sunday and Monday.
11. Counting museums open every day of the week.
12. Finding the top 5 most popular museums by the number of paintings.
13. Finding the top 5 most popular artists by the number of paintings.
14. Identifying the least popular canvas sizes.
15. Finding the museum open for the longest hours in a day.
16. Identifying the museum with the most number of popular painting styles.
17. Finding artists with paintings displayed in multiple countries.
18. Identifying the country and city with the most number of museums.
19. Finding the artist and museum with the most expensive and least expensive painting.
20. Identifying the country with the 5th highest number of paintings.
21. Finding the most and least popular painting styles.
22. Identifying the artist with the most number of portrait paintings outside the USA.

## 📝 Summary of Analysis

The analysis provided several interesting insights into the museum dataset. It revealed that some paintings are not displayed in any museums and highlighted museums that lack any paintings. Price analysis showed that several paintings have asking prices significantly higher or lower than their regular prices. The most expensive canvas size was identified, and duplicate records were effectively removed from various tables. Furthermore, the top 10 most famous painting subjects were determined, and the analysis identified the top 5 most popular museums and artists based on the number of paintings. The museum with the longest open hours and the artist with the most portrait paintings outside the USA were also identified, along with insights into the popularity of different painting styles and the distribution of museums across various cities and countries.

## 🚀 How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Gagann01/museum-data-analysis.git
