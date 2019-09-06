<?php

$times = 1000000;
$result = 1;
$time_start = microtime(TRUE);
for($i = 0; $i < $times; $i++) {
    if($result == 0) {
        $result = 1;
    } else {
        $result = (10*2)/$result;
    }
}
$time_end = microtime(TRUE);

echo "Calculation output in PHP in " . (($time_end - $time_start)*1000) . " ms";
