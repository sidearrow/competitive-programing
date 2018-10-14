<?php
namespace DesignPatternSample;

require_once(__DIR__ . '/Iterator.php');

class StationListIterator implements Iterator {
    private $stationList;
    private $index;

    function __construct($stationList) {
        $this->stationList = $stationList;
        $this->index = 0;
    }

    public function hasNext() {
        return $this->index < $this->stationList->getLength();
    }

    public function next() {
        $station = $this->stationList->getStation($this->index);
        $this->index++;
        return $station;
    }
}