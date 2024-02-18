from rest_framework import serializers


class PlaceValidator:
    """
    Place is choice. It can only be "Indoor" or "Outdoor".
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        place = value.get(self.field)
        if place not in ("Indoor", "Outdoor"):
            raise serializers.ValidationError(f"{place} not a correct place. It has to be Indoor or Outdoor")


class TimeToCompleteValidator:
    """
    The execution time should be no longer than 120 seconds.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_to_complete = value.get(self.field)
        if time_to_complete > 120:
            raise serializers.ValidationError("No more than 120 seconds!")


class PeriodicityValidator:
    """
    A habit cannot be performed less frequently than once every 7 days.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodicity = value.get(self.field)
        if periodicity > 7:
            raise serializers.ValidationError("Maximally on weekly rotation!")


class EnjoyableRewardValidator:
    """
    Eliminate simultaneous selection of a related habit and reward indication.
    """
    def __call__(self, data):
        enjoyable = data.get('enjoyable', False)
        reward = data.get('reward', False)

        if enjoyable and reward:
            raise serializers.ValidationError("If 'enjoyable' is True, 'reward' cannot be True.")

