year_born = ("Paris Hiltn", 1981)

Julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

print (Julia[2])

b = ("Bob", 19, "CS")

(name, age, studies) = b

print (b)


def f(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)

Julia_more_info = ( ("Julia", "Roberts"), (8, "October", 1967),
                     "Actress", ("Atlanta", "Georgia"),
                     [ ("Duplicity", 2009),

                      ("Notting Hill", 1999),
                       ("Pretty Woman", 1990),
                       ("Erin Brockovich", 2000),
                       ("Eat Pray Love", 2010),
                       ("Mona Lisa Smile", 2003),
                       ("Oceans Twelve", 2004) ])
