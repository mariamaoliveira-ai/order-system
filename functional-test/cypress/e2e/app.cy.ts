describe('application shell', () => {
  it('loads the frontend', () => {
    cy.visit('/')
    cy.get('h1').should('contain', 'Order System')
  })
})
