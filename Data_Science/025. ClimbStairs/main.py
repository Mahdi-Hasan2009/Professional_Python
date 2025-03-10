def ways(stairs):
  # Check corner case
  if stairs < 0:
    return 0
  # If no stairs left just return 1 we reach the top
  if stairs == 0:
    return 1
  two_steps = 0
  one_step = 0
  
  if stairs >= 2:
    two_steps = ways(stairs - 2)
  one_step = ways(stairs - 1)
  
  return two_steps + one_step