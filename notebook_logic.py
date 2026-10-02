from starter import ZONES, TIME_BLOCKS, COSTS, PROMISE, delivery_times
import numpy as np
from starter import ZONES, TIME_BLOCKS, COSTS, PROMISE, delivery_times

def cost_per_late_order(costs):
  refund = costs["refund"]
  churn = costs["churn_orders"]
  margin = costs["margin"]
  return refund + churn * margin

def net_profit(zone, time_block, promise, costs):
  times = delivery_times(zone, time_block, promise)
  n_orders = len(times)
  n_late = (times > promise).sum()
  profit = n_orders * costs["margin"]
  late_cost = n_late * cost_per_late_order(costs)
  return profit - late_cost

def best_promise(zone, time_block, promises, costs):
  profits = [net_profit(zone, time_block, p, costs) for p in promises]
  best = int(np.argmax(profits))
  return promises[best], profits[best]