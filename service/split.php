<?php

function tempdir($dir = false, $prefix = '') {
    $tempfile = tempnam($dir, $prefix);
    if (file_exists($tempfile)) { unlink($tempfile); }
    mkdir($tempfile);
    if (is_dir($tempfile)) { return $tempfile; }
}

if(isset($_FILES['image']['name'])){
	$tmp = $_FILES['image']['tmp_name']; 
	$name = $_FILES['image']['name'];  

	if( !is_uploaded_file($tmp) || !move_uploaded_file($tmp, $name) ){
		echo "FAILED TO UPLOAD " . $_FILES['image']['name'] .
			"<br>Temporary Name: $tmp <br>";
	}else{
		$script = getcwd().'/../img2bits.py';
		$result = tempdir('./result');
		$x1 = $_POST['x1'];
		$y1 = $_POST['y1'];
		$x2 = $_POST['x2'];
		$y2 = $_POST['y2'];
		system("python $script $name $x1 $y1 $x2 $y2 $result");
	} 
}else{
	echo "You need to select a file.  Please try again.";
	exit();
}

$bits = explode('.', $name);
$name = $bits[0];
$ext = $bits[1];
$sides = array('l', 'r', 't', 'b', 'c', 'tl', 'tr', 'bl', 'br');
foreach($sides as $side):
?>
<img src="<?php echo "$result/$name-$side.$ext";?>" />
<?php endforeach;?>