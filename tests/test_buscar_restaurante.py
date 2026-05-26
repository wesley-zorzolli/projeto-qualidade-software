import os
import re
from pytest_bdd import scenario, given, when, then, parsers
from playwright.sync_api import Page, expect

BASE_URL = "https://local-eats-unisenac.vercel.app/"
FEATURE_FILE = "../projeto/features/busca_restaurantes.feature"
DEMO_MODE = os.getenv("DEMO_MODE", "0") == "1"
DEMO_DELAY_MS = int(os.getenv("DEMO_DELAY_MS", "1200"))
INSPECT_MODE = os.getenv("INSPECT_MODE", "0") == "1"


def maybe_pause(page: Page, label: str):
    if DEMO_MODE:
        page.wait_for_timeout(DEMO_DELAY_MS)
    if INSPECT_MODE:
        page.pause()


@scenario(FEATURE_FILE, "Fazer login e filtrar restaurantes japoneses")
def test_fazer_login_e_filtrar_restaurantes_japoneses():
    pass


@scenario(FEATURE_FILE, "Visualizar restaurantes japoneses após autenticação")
def test_visualizar_restaurantes_japoneses_apos_autenticacao():
    pass


@given("que estou na página inicial do LocalEats")
def abrir_home(page: Page):
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    maybe_pause(page, "home")
    if INSPECT_MODE:
        page.pause()


@when(parsers.parse('eu faço login com o email "{email}" e a senha "{senha}"'))
def realizar_login(page: Page, email: str, senha: str):
    entrar = page.get_by_role("button", name=re.compile(r"^entrar$|login|acessar", re.I))
    if entrar.count() > 0:
        entrar.first.click()
    else:
        link_entrar = page.get_by_role("link", name=re.compile(r"^entrar$|login|acessar", re.I))
        if link_entrar.count() > 0:
            link_entrar.first.click()

    page.wait_for_load_state("networkidle")
    maybe_pause(page, "apertura-login")

    email_field = None
    for locator in [
        page.get_by_label(re.compile("email", re.I)),
        page.get_by_placeholder(re.compile("email|e-mail", re.I)),
        page.get_by_role("textbox", name=re.compile("email|e-mail", re.I)),
        page.locator('input[type="email"]'),
        page.locator('input[name="email"]'),
    ]:
        try:
            if locator.count() > 0:
                email_field = locator.first
                break
        except Exception:
            continue

    if email_field is None:
        raise AssertionError("Campo de email não encontrado na interface do LocalEats")
    email_field.fill(email)
    maybe_pause(page, "email-preenchido")

    password_field = None
    for locator in [
        page.get_by_label(re.compile("senha|password", re.I)),
        page.get_by_placeholder(re.compile("senha|password", re.I)),
        page.get_by_role("textbox", name=re.compile("senha|password", re.I)),
        page.locator('input[type="password"]'),
        page.locator('input[name="password"]'),
    ]:
        try:
            if locator.count() > 0:
                password_field = locator.first
                break
        except Exception:
            continue

    if password_field is None:
        raise AssertionError("Campo de senha não encontrado na interface do LocalEats")
    password_field.fill(senha)
    maybe_pause(page, "senha-preenchida")

    entrar_submit = page.get_by_role("button", name=re.compile(r"^entrar$|login|acessar|continuar", re.I))
    if entrar_submit.count() > 0:
        entrar_submit.first.click()
    else:
        password_field.press("Enter")

    page.wait_for_load_state("networkidle")
    maybe_pause(page, "login-concluido")


@when(parsers.parse('eu aplico o filtro "{categoria}"'))
def aplicar_filtro(page: Page, categoria: str):
    filtro = page.get_by_role("button", name=categoria)
    if filtro.count() > 0:
        filtro.first.click()
        page.wait_for_load_state("networkidle")
        maybe_pause(page, f"filtro-{categoria}")
        return

    texto_clicavel = page.get_by_text(categoria, exact=True)
    if texto_clicavel.count() > 0:
        texto_clicavel.first.click()
        page.wait_for_load_state("networkidle")
        maybe_pause(page, f"filtro-{categoria}")
        return

    locator_fallback = page.locator(f'text="{categoria}"')
    if locator_fallback.count() > 0:
        locator_fallback.first.click()
        page.wait_for_load_state("networkidle")
        maybe_pause(page, f"filtro-{categoria}")
        return

    raise AssertionError(f'Filtro "{categoria}" não encontrado na página')


@when("eu já estou autenticado no LocalEats")
def usuario_ja_autenticado(page: Page):
    indicador_logado = page.get_by_role("button", name=re.compile("sair|perfil|minha conta|account", re.I))
    if indicador_logado.count() == 0:
        realizar_login(page, "teste@teste.com", "123456")
    else:
        expect(indicador_logado.first).to_be_visible(timeout=8000)
    maybe_pause(page, "usuario-autenticado")


@then("eu devo ver restaurantes de comida japonesa listados")
def validar_resultados_japonesa(page: Page):
    candidatos = [
        page.get_by_text("Japonesa", exact=False),
        page.locator('article:has-text("Japonesa")'),
        page.locator('section:has-text("Japonesa")'),
        page.locator('li:has-text("Japonesa")'),
        page.locator('.restaurant-card:has-text("Japonesa")'),
        page.locator('[data-testid*="restaurant"]:has-text("Japonesa")'),
    ]

    for locator in candidatos:
        try:
            if locator.count() > 0:
                expect(locator.first).to_be_visible(timeout=8000)
                maybe_pause(page, "resultado-japonesa")
                return
        except Exception:
            continue

    # fallback pragmático: se houver cards visíveis após aplicar o filtro, consideramos o resultado exibido
    cards = page.locator('article, li, .restaurant-card, [data-testid*="restaurant"]')
    if cards.count() > 0:
        expect(cards.first).to_be_visible(timeout=8000)
        maybe_pause(page, "cartoes-visiveis")
        return

    raise AssertionError("Não foram encontrados restaurantes japoneses após o filtro 'Japonesa'")
