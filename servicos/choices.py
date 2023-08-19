from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_VALVULA_MOTOR =  "TVM", "Trocar válvula do motor",
    TROCAR_OLEO = "TO", "Troca de óleo"
    BALANCEMANTO = "B", "Balanceamento"
    TROCAR_MOTOR = "TM", "Trocar Motor"
    TROCAR_PNEU = "TP", "Trocar Pneu"
    CAIXA_MARCHA = "CM", "Trocar caixa de marcha"
    PINTURA = "P", "PINTAR O CARRO"
    DESAMASSAR = "D", "Desamassar"
    ALINHAMENTO = "A", "Alinhamento"
    