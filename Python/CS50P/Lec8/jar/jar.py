class Jar:
    def __init__(this, capacity=12):
        this._size = 0
        if capacity < 0:
            raise ValueError("Invalid capacity")
        this._capacity = capacity

    def __str__(this):
        num = this.size * "🍪"
        return num

    def deposit(this, n):
        if this.size + n > this.capacity:
            raise ValueError("Exceeded capacity")
        this._size += n

    def withdraw(this, n):
        if n > this.size:
            raise ValueError("No enough cookies")
        this._size -= n


    @property
    def capacity(this):
        return this._capacity

    @property
    def size(this):
        return this._size
