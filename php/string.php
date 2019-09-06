<?php

$times = 1000000;
$string = "Hello Euro Python 2019!";
$time_start = microtime(TRUE);
for($i = 0; $i < $times; $i++) {
    $string = "Hello Euro Python 2019!";
}
$time_end = microtime(TRUE);

echo "String output in PHP in " . (($time_end - $time_start)*1000) . " ms";
