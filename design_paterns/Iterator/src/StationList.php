<?php
namespace DesignPatternSample;

require_once(__DIR__ . '/Aggregate.php');
require_once(__DIR__ . '/StationListIterator.php');

class StationList implements Aggregate {
    private $stationList;
    private $last = 0;

    function __construct() {
        $this->stationList = [];
    }

    public function getStation($index) {
        return $this->stationList[$index];
    }

    public function appendStation($station) {
        $this->stationList[] = $station;
        $this->last++;
    }

    public function getLength() {
        return $this->last;
    }

    public function iterator() {
        return new StationListIterator($this);
    }
}