from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = "Popula o banco com dados iniciais"

    def handle(self, *args, **options):
        self._seed_salas()
        self._seed_convenios()
        self._seed_especialidades()
        self._seed_categorias()
        self._seed_leitos()
        self.stdout.write(self.style.SUCCESS("Dados iniciais criados com sucesso!"))

    def _seed_salas(self):
        from apps.rooms.models import SalaCirurgica
        if SalaCirurgica.objects.exists():
            self.stdout.write(" -> Salas ja existem, pulando...")
            return
        for i in range(1, 13):
            SalaCirurgica.objects.create(
                numero=str(i),
                nome=f"Sala Cirúrgica {i}",
                valor_hora=1875.00 if i <= 6 else 2500.00,
                status="disponivel",
            )
        self.stdout.write(f" -> {12} salas cirurgicas criadas")

    def _seed_convenios(self):
        from apps.patients.models import Convenio
        if Convenio.objects.exists():
            self.stdout.write(" -> Convenios ja existem, pulando...")
            return
        convenios = [
            ("Unimed", "UNIMED"),
            ("Bradesco Saúde", "BRADESCO"),
            ("Amil", "AMIL"),
            ("SulAmérica", "SULAMERICA"),
            ("NotreDame Intermédica", "ND"),
            ("Particular", "PARTICULAR"),
        ]
        for nome, codigo in convenios:
            Convenio.objects.create(nome=nome, codigo=codigo)
        self.stdout.write(f" -> {len(convenios)} convenios criados")

    def _seed_especialidades(self):
        from apps.doctors.models import Especialidade
        if Especialidade.objects.exists():
            self.stdout.write(" -> Especialidades ja existem, pulando...")
            return
        especialidades = [
            ("Cirurgia Geral", "CG"),
            ("Cirurgia Cardíaca", "CC"),
            ("Cirurgia Ortopédica", "CO"),
            ("Cirurgia Neurológica", "CN"),
            ("Cirurgia Pediátrica", "CP"),
            ("Cirurgia Plástica", "CPL"),
            ("Cirurgia Vascular", "CV"),
            ("Cirurgia Torácica", "CT"),
            ("Cirurgia Oncológica", "CON"),
            ("Cirurgia Urológica", "CU"),
            ("Cirurgia Oftalmológica", "COF"),
            ("Cirurgia Bariátrica", "CB"),
        ]
        for nome, codigo in especialidades:
            Especialidade.objects.create(nome=nome, codigo=codigo)
        self.stdout.write(f" -> {len(especialidades)} especialidades criadas")

    def _seed_categorias(self):
        from apps.materials.models import CategoriaMaterial
        if CategoriaMaterial.objects.exists():
            self.stdout.write(" -> Categorias ja existem, pulando...")
            return
        categorias = [
            "Fios Cirúrgicos",
            "Lâminas e Bisturis",
            "Sondas e Cateteres",
            "Luvas Cirúrgicas",
            "Compressas e Gazes",
            "Medicamentos",
            "Implantes Ortopédicos",
            "Materiais de Osteossíntese",
            "Drenos",
            "Equipamentos",
        ]
        for nome in categorias:
            CategoriaMaterial.objects.create(nome=nome)
        self.stdout.write(f" -> {len(categorias)} categorias criadas")

    def _seed_leitos(self):
        from apps.admissions.models import Leito
        if Leito.objects.exists():
            self.stdout.write(" -> Leitos ja existem, pulando...")
            return
        alas = ["A", "B", "C"]
        for ala in alas:
            for numero in range(1, 11):
                Leito.objects.create(
                    numero=f"{ala}{numero:02d}",
                    ala=f"Ala {ala}",
                )
        self.stdout.write(f" -> {30} leitos criados")
