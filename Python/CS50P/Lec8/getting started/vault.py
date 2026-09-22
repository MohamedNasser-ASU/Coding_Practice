class Vault:
    def __init__(this, galleons=0, sickles=0, knuts=0):
        this.galleons = galleons
        this.sickles = sickles
        this.knuts = knuts

    def __str__(this):
        return f"{this.galleons} galleons, {this.sickles} sickles, {this.knuts} knuts"

    def __add__(this, that):
        galleons = this.galleons + that.galleons
        sickles = this.sickles + that.sickles
        knuts = this.knuts + that.knuts
        return Vault(galleons, sickles, knuts)

potter = Vault(100,50,20)
weasley = Vault(25, 100, 80)
print(potter , "\n" , weasley, "\n" , potter+weasley , sep="")








