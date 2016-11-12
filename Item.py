class Item:
    def __init__(self):
        self.type = None  # the type (or "class") of weapon (laser, bullets, melee, etc)
        self.projectile = None  # what projectile to shoot

        self.ammo = 0  # how much ammo the weapon has
        self.clipSize = 0  # the total size of the clip
        self.clip = 0  # how much ammo is left in the clip

        self.rateOfFire = -1  # how fast can this weapon shoot
        self.reloadTime = -1  # how long does it take to reload

    def shoot(self):
        self.clip -= 1  # fired a shot

    def reload(self):
        # calculate the amount of ammo to add to the clip
        ammoToReload = self.clipSize - self.clip

        # in case there wasn't enough ammo left
        if ammoToReload > self.ammo:
            ammoToReload = self.ammo

        # reload
        self.clip += ammoToReload
        self.ammo -= ammoToReload
