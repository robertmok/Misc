<?php 
session_start();
?>
<!DOCTYPE HTML>
<html>
<body>
You picked <?php echo $_POST["dim1"]; ?> x <?php echo $_POST["dim2"]; ?> multiplication table. <br>
<br>
<?php
$dim1 = $_POST["dim1"];
$dim2 = $_POST["dim2"];
$table = array(array());
for ($x = 1; $x <= $dim1; $x++){
	for ($y = 1; $y <= $dim2; $y++){
		$table[$x-1][$y-1] = $x* $y;
		//echo $table[$x-1][$y-1]." ";
	}
}

echo '<table border="1">';
for ($x = 0; $x < count($table); $x++){
	echo '<tr>';
	for ($y = 0; $y < count($table[$x]); $y++){
		echo "<td>{$table[$x][$y]}</td>";
	}
	echo '</tr>';
}
echo '</table>';

if(isset($_SESSION['views']))
	$_SESSION['views'] = $_SESSION['views']+1;
else
	$_SESSION['views'] = 1;
echo "Views count = ". $_SESSION['views'];

//session_unset();
//session_destroy();

?>

</body>
</html>
