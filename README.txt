-Sharks and Jets-

Source code changed:
- Flock 
    - Added the class variable flock_other and method
      registerFlockOther which serves a similar purpose as the class 
      variables leader and predator and their corresponding register 
      methods. 
- Bird
    - Added an additional initialization variable, flock_other, 
      which defaults to None if given no input.
    - Added the method computeTribal which uses the flock_other
      input to try to avoid the flock that is not its own if 
      flock_other exists.
    - Modified the steer method to take computeTribal into account
      when calculating the weighted average of the concerns' directions.

Shark and Jet classes:
- Both these classes inherit from Bird and have no additional methods.
  They just override the color method to have distinct colors from each
  other.

sim7.py:
- When running the simulation, you should notice that the Sharks (light
  yellow) and the Jets (purple) avoid each other and like to stick with 
  birds in their own flock. They are repelled by members of the other flock
  and compelled to be with members of their own flock.

