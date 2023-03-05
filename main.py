# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


# ------------------------------------------------------------------------------
#  parameters -
#    name {string}
#    greeting {string} default = "Hello, <name>!"
#  return - greeting with placeholder ("<name>") replaced with name argument
# ------------------------------------------------------------------------------

def greet(name, greeting="Hello, <name>!"):
    return greeting.replace("<name>", name)


# ------------------------------------------------------------------------------
#  parameters -
#    mass {float}
#    body {string} default = "earth"
#  return -
#    force applied to a given mass by a given celestial body.
#    If a non valid body is given returns None
# ------------------------------------------------------------------------------
def force(mass, body="earth"):
    gravitational_factor = {
        "sun": 274,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6,
    }
    body = body.lower()
    if (body not in gravitational_factor):
        return None
    return gravitational_factor[body] * mass


# ------------------------------------------------------------------------------
#  parameters -
#    m1 {float} - mass of first body in kg
#    m2 {float} - mass of second body in kg
#    d {float} - distance between to bodies in meters
#  return -
#    gravitational force between to bodies
# ------------------------------------------------------------------------------
def pull(m1, m2, d):
    g = 6.674e-11
    return g * ((m1 * m2) / (d ** 2))
