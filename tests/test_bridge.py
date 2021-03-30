import pytest
from Car import Car


class TestBridgeHappy:

    def test_total_weight_under_30000(self, bridge):
        assert bridge.calc_total_weight() == 0

    def test_adding_motorbike_to_empty_bridge(self, bridge, default_motorbike):
        bridge.add_vehicle(default_motorbike)
        assert len(bridge.vehicles) == 1

    def test_adding_car_to_empty_bridge(self, bridge, lorry):
        bridge.add_vehicle(lorry)
        assert len(bridge.vehicles) == 1

    def test_adding_lorry_to_empty_bridge(self, bridge, car):
        bridge.add_vehicle(car)
        assert len(bridge.vehicles) == 1

    def test_adding_20_motorbikes_to_empty_bridge(self, bridge, default_motorbike):
        for _ in range(0, 20, 1):
            bridge.add_vehicle(default_motorbike)
        assert len(bridge.vehicles) == 20

    def test_max_weight_limit_of_the_bridge(self, bridge):
        car = Car("5253", 29999)
        bridge.add_vehicle(car)
        assert bridge.calc_total_weight() == 29999

    def test_max_weight_limit_of_the_bridge_2_actual_vehicle_added(self, bridge):
        car = Car("5253", 29999)
        bridge.add_vehicle(car)
        assert bridge.vehicles[0] == car

    def test_remove_car(self, bridge, car, default_motorbike):
        bridge.add_vehicle(car)
        bridge.add_vehicle(default_motorbike)
        bridge.remove_car("5050")
        assert len(bridge.vehicles) == 1


class TestBridgeSad:
    pass
