(define (domain warehouse)
  (:requirements :strips :typing)

  (:types
    robot package location - object
  )

  (:predicates
    (at-robot ?r - robot ?l - location)
    (at-package ?p - package ?l - location)
    (in-robot ?p - package ?r - robot)
    (robot-free ?r - robot)
    (connected ?l1 - location ?l2 - location)
  )

  (:action move
    :parameters (?r - robot ?from - location ?to - location)
    :precondition (and
      (at-robot ?r ?from)
      (connected ?from ?to)
    )
    :effect (and
      (not (at-robot ?r ?from))
      (at-robot ?r ?to)
    )
  )

  (:action pickup
    :parameters (?r - robot ?p - package ?l - location)
    :precondition (and
      (at-robot ?r ?l)
      (at-package ?p ?l)
      (robot-free ?r)
    )
    :effect (and
      (not (at-package ?p ?l))
      (in-robot ?p ?r)
      (not (robot-free ?r))
    )
  )

  (:action drop
    :parameters (?r - robot ?p - package ?l - location)
    :precondition (and
      (at-robot ?r ?l)
      (in-robot ?p ?r)
    )
    :effect (and
      (not (in-robot ?p ?r))
      (at-package ?p ?l)
      (robot-free ?r)
    )
  )
)
