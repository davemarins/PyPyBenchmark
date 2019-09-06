<?php

$times = 1000000;
$arr = array(
    'userId' => 1,
    'id' => 2,
    'title' => 'delectus aut autem',
    'completed' => FALSE
);
$json = json_encode($arr);
$time_start = microtime(TRUE);
for($i = 0; $i < $times; $i++) {
    $new_array = json_decode($json, TRUE);
}
$time_end = microtime(TRUE);

echo "JSON output in PHP in " . (($time_end - $time_start)*1000) . " ms";
