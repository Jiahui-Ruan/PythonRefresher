# *args will be transform to a list, so we are able to use sum on them
def addition_simplified(*args):
    return sum(args)

##

# first one is called position arguments, and second one is called
# keyword arguments, we cannot change their position
def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(12, 13, 55, name="Jose", location="UK")
