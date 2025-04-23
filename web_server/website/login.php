<?php
$servername = "mysql_db";
$username = "root";
$password = "rootpass";
$dbname = "hardware_store";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get user input **(NO SANITIZATION, FULLY VULNERABLE)**
$user = $_POST['username'];
$pass = $_POST['password'];

// Vulnerable SQL Query (directly concatenates input)
$sql = "SELECT * FROM users WHERE username = '$user' AND password = '$pass'";
$result = $conn->query($sql);

// Check if login is successful
if ($result->num_rows > 0) {
    echo "Login successful!";
} else {
    echo "Invalid username or password.";
}

$conn->close();
?>
