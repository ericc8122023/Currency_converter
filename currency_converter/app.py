import dearpygui.dearpygui as dpg
import model

def convert():
    """ get exchange rate & multipy by amount """
    amount = dpg.get_value(amount_id)
    from_cur = dpg.get_value(from_cur_id)
    to_cur = dpg.get_value(to_cur_id)


    from_cur = from_cur.split("-")[0].strip()
    to_cur = to_cur.split("-")[0].strip()


    status, rate = model.get_exchange_rate(from_cur, to_cur)
    exchange = amount * rate
    results = "{} {} is equal to {} {}".format(amount, from_cur, exchange, to_cur)
    dpg.set_value(output_id,results)

dpg.create_context()

amount_id = dpg.generate_uuid()
from_cur_id = dpg.generate_uuid()
to_cur_id = dpg.generate_uuid()
output_id = dpg.generate_uuid()

dpg.create_viewport(title='Currency Converter', width=600, height=300)

with dpg.window(label="Currency Converter", width=600, height=300):
    dpg.add_text("Welcome to the Currency Converter,")
    dpg.add_input_float(label="Amount", default_value=1.0, width=100,
      tag = amount_id, min_value =0.01, min_clamped=True)
    dpg.add_combo(model.currencies, default_value=model.default_from, 
      tag =from_cur_id,  label ="From" , width =250)
    dpg.add_combo(model.currencies, default_value=model.default_to, 
      tag = to_cur_id,  label ="To" , width =250)
    dpg.add_button(label="Convert", callback = convert)
    dpg.add_text("", width=300, tag = output_id)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()