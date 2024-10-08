from django.db import models

class Champion(models.Model):
    code = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    games = models.PositiveIntegerField()
    wins = models.PositiveIntegerField()
    winrate = models.DecimalField(max_digits=5, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        if self.games > 0:
            self.winrate = (self.wins / self.games) * 100
        else:
            self.winrate = 0.00
        super().save(*args, **kwargs)

    def __str__(self):
        return f"code: {self.code}, name: {self.name}, winrate: {self.winrate}"

class Items(models.Model):
    item1 = models.PositiveIntegerField()
    item2 = models.PositiveIntegerField()
    item3 = models.PositiveIntegerField()
    item4 = models.PositiveIntegerField()
    games = models.PositiveIntegerField()
    wins = models.PositiveIntegerField()
    winrate = models.DecimalField(max_digits=5, decimal_places=2, editable=False)
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE, to_field='code')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['item1', 'item2', 'item3', 'item4', 'champion'],
                name='unique_items_per_champion'
            )
        ]

    def save(self, *args, **kwargs):
        if self.games > 0:
            self.winrate = (self.wins / self.games) * 100
        else:
            self.winrate = 0.00
        super().save(*args, **kwargs)

    def __str__(self):
        return f"winrate: {self.winrate}"

class Prismatic_item(models.Model):
    code = models.PositiveIntegerField()
    games = models.PositiveIntegerField()
    wins = models.PositiveIntegerField()
    winrate = models.DecimalField(max_digits=5, decimal_places=2, editable=False)
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE, to_field='code')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['code', 'champion'],
                name='unique_prismatic_per_champion'
            )
        ]

    def save(self, *args, **kwargs):
        if self.games > 0:
            self.winrate = (self.wins / self.games) * 100
        else:
            self.winrate = 0.00
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"code: {self.code}, champion: {self.champion}"
    
class Initial_item(models.Model):
    code = models.PositiveIntegerField()
    games = models.PositiveIntegerField()
    wins = models.PositiveIntegerField()
    winrate = models.DecimalField(max_digits=5, decimal_places=2, editable=False)
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE, to_field='code')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['code', 'champion'],
                name='unique_initial_item_per_champion'
            )
        ]

    def save(self, *args, **kwargs):
        if self.games > 0:
            self.winrate = (self.wins / self.games) * 100
        else:
            self.winrate = 0.00
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"code: {self.code}, champion: {self.champion}"
    
class Boot_item(models.Model):
    code = models.PositiveIntegerField()
    games = models.PositiveIntegerField()
    wins = models.PositiveIntegerField()
    winrate = models.DecimalField(max_digits=5, decimal_places=2, editable=False)
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE, to_field='code')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['code', 'champion'],
                name='unique_boot_item_per_champion'
            )
        ]

    def save(self, *args, **kwargs):
        if self.games > 0:
            self.winrate = (self.wins / self.games) * 100
        else:
            self.winrate = 0.00
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"code: {self.code}, champion: {self.champion}"

class Prismatic_augment(models.Model):
    code = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    api_name = models.CharField(max_length=300, default="acceleratingsorcery_large.png")
    games = models.PositiveIntegerField()
    wins = models.PositiveIntegerField()
    winrate = models.DecimalField(max_digits=5, decimal_places=2, editable=False)
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE, to_field='code')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['code', 'champion'],
                name='unique_prismatic_augment_per_champion'
            )
        ]

    def save(self, *args, **kwargs):
        if self.games > 0:
            self.winrate = (self.wins / self.games) * 100
        else:
            self.winrate = 0.00
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"code: {self.code}, champion: {self.champion}"

class Gold_augment(models.Model):
    code = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    api_name = models.CharField(max_length=300, default="acceleratingsorcery_large.png")
    games = models.PositiveIntegerField()
    wins = models.PositiveIntegerField()
    winrate = models.DecimalField(max_digits=5, decimal_places=2, editable=False)
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE, to_field='code')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['code', 'champion'],
                name='unique_gold_augment_per_champion'
            )
        ]

    def save(self, *args, **kwargs):
        if self.games > 0:
            self.winrate = (self.wins / self.games) * 100
        else:
            self.winrate = 0.00
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"code: {self.code}, champion: {self.champion}"
    
class Silver_augment(models.Model):
    code = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    api_name = models.CharField(max_length=300, default="acceleratingsorcery_large.png")
    games = models.PositiveIntegerField()
    wins = models.PositiveIntegerField()
    winrate = models.DecimalField(max_digits=5, decimal_places=2, editable=False)
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE, to_field='code')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['code', 'champion'],
                name='unique_silver_augment_per_champion'
            )
        ]

    def save(self, *args, **kwargs):
        if self.games > 0:
            self.winrate = (self.wins / self.games) * 100
        else:
            self.winrate = 0.00
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"code: {self.code}, champion: {self.champion}"

class Match(models.Model):
    code = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return f"{self.code}"