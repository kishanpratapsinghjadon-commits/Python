#problem = customize a coffee order "small", "medium", or "large" with an option for "extra shot" of expresso.
order_size = "medium"
extra_shot = True
if extra_shot:
    coffee = order_size + "coffee with an extra shot"
else:
    coffee = oeder_size + "coffee"

print("order:", coffee)