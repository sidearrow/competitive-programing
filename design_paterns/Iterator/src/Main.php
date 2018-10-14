<?php
namespace DesignPatternSample;

require_once(__DIR__ . '/Station.php');
require_once(__DIR__ . '/StationList.php');

$stationList = new StationList();

$stationList->appendStation(new Station('Tennouji'));
$stationList->appendStation(new Station('Shin-imamiya'));

$stationListIterator = $stationList->iterator();

while ($stationListIterator->hasNext()) {
    $station = $stationListIterator->next();
    echo $station->getName();
    echo "\n";
}