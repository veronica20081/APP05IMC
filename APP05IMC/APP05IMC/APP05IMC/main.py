import flet as ft

def calcular_imc(txtPeso,txtAltura,lblIMC,page):
    try:
        peso=float(txtPeso.value)
        altura=float(txtAltura.value)
        imc=peso/(altura**2)
        lblIMC.value=f"Tu IMC es de: {imc:.2f}"
        page.update()
        
        #Funcion para cerrar el cuadro de dialogo y actualizar la pagina
        def cerrar_dialogo(e):
            page.dialog.open = False
            page.updape()
            
            # Validacion del IMC
            if imc<18.5:
                dialog=ft.AlertDialog(
                    title="Bajo peso",
                    content="Tu IMC indica que tienes bajo peso",
                    actions=[
                        ft.TexButton(text="Cerrar")
                    ]
                )
            elif imc>=18.5 and imc<24.9:
                dialog=ft.AlertDialog(
                    title="Peso normal",
                    content="Tu IMC indica que tienes un peso normal",
                    actions=[
                        ft.TextButton(text="Cerrar",on_click=cerrar_dialodo)
                    ]
                )
            elif imc>=25 and imc<30:
                dialog=ft
def main(page: ft.Page):
    page.title = "Calculadora de IMC" 
    page.bgcolor="pink"
    
    txtPeso=ft.TextField(label="Ingresa tu peso")
    txtAltura=ft.TextField(label="Ingresa tu altura")
    lblIMC=ft.Text("Tu IMC es de: ")
    
    img=ft.Image(
        src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )

    btnCalcular=ft.ElevatedButton(text="Calculadora")
    btnLimpiar=ft.ElevatedButton(text="Limpiar")
    
    page.add(
        ft.Column(
            controls=[
                txtPeso,txtAltura,lblIMC
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                img
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                btnCalcular,btnLimpiar
            ],alignment="CENTER")
    )
        
    
    


ft.app(target=main,view=ft.AppView.WEB_BROWSER)