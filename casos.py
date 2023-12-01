from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

def T01(driver,email,senha):
  # Caso de teste T01
  botao_login = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
  botao_login.click()

  campo_email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email")))
  campo_email.send_keys(email)
  campo_senha = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
  campo_senha.send_keys(senha)

  botao_logar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and contains(text(), "Submit")]')))
  driver.execute_script("arguments[0].scrollIntoView(true);", botao_logar)
  sleep(2)
  botao_logar.click()

  sleep(5)

def T02(driver):
  # Caso de teste T02
  botao_login = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
  botao_login.click()

  campo_email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email")))
  campo_email.send_keys("teste30@gmail.com.br")
  campo_senha = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
  campo_senha.send_keys("t!!!!!!!")

  sleep(2)

  botao_logar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and contains(text(), "Submit")]')))
  driver.execute_script("arguments[0].scrollIntoView(true);", botao_logar)
  sleep(2)
  botao_logar.click()

def T05(driver):
  # Caso de teste T05
  T01(driver,"lucas.oliveira@teste.com","lucas.oliveira")

  produto = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/div/div[3]/div/a')))
  produto.click()

  botao_adicionar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="button" and contains(text(), "Add To Cart")]')))
  botao_adicionar.click()

  sleep(2)

def T03(driver):
  T05(driver)

  #Caso de teste T03
  botao_finalizar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="button" and contains(text(), "Checkout")]')))
  botao_finalizar.click()

  campo_endereco = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "address")))
  campo_endereco.send_keys("Rua dos Lobos, 766")

  campo_cidade = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "city")))
  campo_cidade.send_keys("Russas")

  campo_codigoPostal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "postalCode")))
  campo_codigoPostal.send_keys("62900-000")

  campo_pais = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "country")))
  campo_pais.send_keys("Brasil")

  botao_enviar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and contains(text(), "Submit")]')))
  driver.execute_script("arguments[0].scrollIntoView(true);", botao_enviar)
  sleep(2)
  botao_enviar.click()

  botao_fechar_pedido = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="button" and contains(text(), "Place order")]')))
  sleep(2)
  botao_fechar_pedido.click()

  botao_pagar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,"StripeCheckout")))
  sleep(2)
  botao_pagar.click()

  sleep(4)
  # Encontre o iframe pelo nome, índice ou elemento
  iframe = driver.find_element(by=By.CLASS_NAME, value='stripe_checkout_app')
  # Alternar para o iframe
  driver.switch_to.frame(iframe)

  campo_email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email")))
  campo_email.send_keys("lucas.oliveira@teste.com")

  campo_cartao_numero = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "card_number")))
  campo_cartao_numero.send_keys("4242")
  campo_cartao_numero.send_keys("4242")
  campo_cartao_numero.send_keys("4242")
  campo_cartao_numero.send_keys("4242")

  campo_cartao_validade = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cc-exp")))
  campo_cartao_validade.send_keys("04")
  campo_cartao_validade.send_keys("2024")


  campo_cartao_cvc = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cc-csc")))
  campo_cartao_cvc.send_keys("333")

  pagar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
  pagar.click()

def T07(driver):
  # caso de teste T07
  T01(driver,"lucas.oliveira@teste.com","lucas.oliveira")

  icone_perfil = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'basic-nav-dropdown')))
  icone_perfil.click()

  botao_perfil = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Profile')))
  sleep(2)
  botao_perfil.click()

  sleep(10)
  icone_olho = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div/div[2]/div/div/table/tbody/tr[1]/td[6]/a')))
  driver.execute_script("arguments[0].click();", icone_olho)

def T08(driver):
  # caso de teste T08
  T01(driver, "davi@teste.com", "123456")

  icone_perfil = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'basic-nav-dropdown')))
  icone_perfil.click()

  botao_perfil = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Profile')))
  sleep(2)
  botao_perfil.click()

def T10(driver):
  botao_registrar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
  botao_registrar.click()

  sleep(2)

  campo_nome = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "name")))
  campo_nome.send_keys("Davi Gomes")

  campo_email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email")))
  campo_email.send_keys("lucas.oliveira@teste.com")
  campo_senha = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
  campo_senha.send_keys("123456")
  
  campo_confirma_senha = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "confirmPassword")))
  campo_confirma_senha.send_keys("123456")

  botao_finalizar_registro = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and contains(text(), "Register")]')))
  driver.execute_script("arguments[0].scrollIntoView(true);", botao_finalizar_registro)
  sleep(2)
  botao_finalizar_registro.click()

def T13(driver):
  # caso de teste T13
  T05(driver)

  icone_adicionar = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="icons__cart  m-2 rounded-circle text-white p-1 cursor-pointer"][1]')))
  icone_adicionar.click()

def T14(driver):
  # caso de teste T13
  T05(driver)

  icone_remover = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="icons__cart m-2 rounded-circle text-white p-1 cursor-pointer "]')))
  icone_remover.click()

def T15(driver):
  T01(driver,"lucas.oliveira@teste.com","lucas.oliveira")

  produto = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/div/div[1]/div/a')))
  produto.click()

  select_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'rating')))
  estrelas = Select(select_element)
  estrelas.select_by_value('3')

  comentario = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'comment')))
  comentario.send_keys("Não gostei")

  botao_submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and contains(text(), "Submit")]')))
  driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", botao_submit)
  sleep(2)
  botao_submit.click()

  sleep(10)




