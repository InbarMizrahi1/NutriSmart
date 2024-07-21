<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NutriSmart</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>NutriSmart</h1>
        <nav>
            <ul>
                <li><a href="#search">Search</a></li>
                <li><a href="#daily-log">Daily Log</a></li>
                <li><a href="#recommendations">Recommendations</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="search">
            <h2>Food Search</h2>
            <input type="text" id="search-bar" placeholder="Search for a food...">
            <div id="search-results"></div>
        </section>
        <section id="daily-log">
            <h2>Daily Intake Log</h2>
            <ul id="log-entries"></ul>
            <button id="add-log-entry">Add Entry</button>
        </section>
        <section id="recommendations">
            <h2>Recommendations</h2>
            <div id="recommendations-content"></div>
        </section>
    </main>
    <script src="app.js"></script>
</body>
</html>
