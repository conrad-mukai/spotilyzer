"""
spotilyzer test mock paginators entry point
"""

# test imports
from .describe_instance_type_offerings \
    import MockDescribeInstanceTypeOfferingsPaginator
from .describe_spot_price_history import MockDescribeSpotPriceHistoryPaginator
from .describe_instance_types import MockDescribeInstanceTypesPaginator


# exports
paginators = {
    'describe_instance_type_offerings':
        MockDescribeInstanceTypeOfferingsPaginator(),
    'describe_spot_price_history': MockDescribeSpotPriceHistoryPaginator(),
    'describe_instance_types': MockDescribeInstanceTypesPaginator()
}
