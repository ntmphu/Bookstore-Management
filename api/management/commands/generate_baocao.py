from django.core.management.base import BaseCommand
from datetime import date
from api.services import generate_baocaoton_for_month, generate_baocaocongno_for_month

class Command(BaseCommand):
    help = "Generate BaoCaoTon report for a given month (default current month)"

    def add_arguments(self, parser):
        parser.add_argument(
            '--month', type=str, help="Month in YYYY-MM format (e.g. 2025-06)"
        )

    def handle(self, *args, **options):
        month_str = options.get('month')
        if month_str:
            year, month = map(int, month_str.split('-'))
            target_month = date(year, month, 1)
        else:
            target_month = None

        baocaoton = generate_baocaoton_for_month(target_month)
        baocaocongno = generate_baocaocongno_for_month(target_month)
        self.stdout.write(self.style.SUCCESS(f"BaoCaoTon generated for {baocaoton.Thang.strftime('%Y-%m')}"))
        self.stdout.write(self.style.SUCCESS(f"BaoCaoCongNo generated for {baocaocongno.Thang.strftime('%Y-%m')}"))
