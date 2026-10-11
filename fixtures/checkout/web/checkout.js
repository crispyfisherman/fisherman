// Illustrative UI boundary. A real HTTP server is outside this fixture.
export async function submitCheckout(api, state) {
  state.status = 'submitting';
  const response = await api('/checkout', {
    order_id: state.orderId,
    sku: state.sku,
    quantity: state.quantity,
  });
  state.status = response.status === 201 ? 'created' : 'failed';
  state.error = response.status === 201 ? null : response.body.error;
  return state;
}
