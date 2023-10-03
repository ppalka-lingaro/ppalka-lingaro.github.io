    erDiagram
          CUSTOMER }|..|{ ADDRESS : has
          CUSTOMER {
            string firstName PK
            string  lastName
            string email FK
            Address shippingAddress
            Address billingAddress
            }
          ADDRESS {
            string streetName
            string streetNumber
            string city
            string zipCode
            string country
            string state
          }
          STORE {
            string name
            string url
            string region
            string brand
            string id
            array products
            array customers
            array orders
          }
          CUSTOMER ||--o{ ORDER : places
          CUSTOMER ||--o{ INVOICE : "liable for"
          ADDRESS ||--o{ ORDER : receives
          INVOICE ||--|{ ORDER : covers
          ORDER ||--|{ "ORDER LINE ITEM" : includes
          ORDER {
            Store store
            Customer customer
            Session session
            string id
            DateTime date
            float total
            float shipping
            float tax
            float discount
            string currency
            PaymentMethod
            ShippingMethod
          }
          "PRODUCT CATEGORY" ||--|{ PRODUCT : contains
          "PRODUCT CATEGORY"{
            string name
            string id
            string ProductCategory
          }
          PRODUCT ||--o{ ORDER-ITEM : "ordered in"
          PRODUCT {
            string sku
            string name
            decimal price
            array categories
            ProductCategory mainCategory
          }
          "GA EVENT" {
            string category
            string action
            string label
            string value
            string session
          }

          "TRAFFIC SOURCE" {
            String name
            bool isPaid
            float costPerC1ick
          }

          "ORDER LINE ITEM" {
            Product product
            Order order
            int  quantity
            float price
            float total
            float discount
            float tax
          }
    erDiagram
          CUSTOMER }|..|{ ADDRESS : has
          CUSTOMER {
            string firstName PK
            string  lastName
            string email FK
            Address shippingAddress
            Address billingAddress
            }
          ADDRESS {
            string streetName
            string streetNumber
            string city
            string zipCode
            string country
            string state
          }
          STORE {
            string name
            string url
            string region
            string brand
            string id
            array products
            array customers
            array orders
          }
          CUSTOMER ||--o{ ORDER : places
          CUSTOMER ||--o{ INVOICE : "liable for"
          ADDRESS ||--o{ ORDER : receives
          INVOICE ||--|{ ORDER : covers
          ORDER ||--|{ "ORDER LINE ITEM" : includes
          ORDER {
            Store store
            Customer customer
            Session session
            string id
            DateTime date
            float total
            float shipping
            float tax
            float discount
            string currency
            PaymentMethod
            ShippingMethod
          }
          "PRODUCT CATEGORY" ||--|{ PRODUCT : contains
          "PRODUCT CATEGORY"{
            string name
            string id
            string ProductCategory
          }
          PRODUCT ||--o{ ORDER-ITEM : "ordered in"
          PRODUCT {
            string sku
            string name
            decimal price
            array categories
            ProductCategory mainCategory
          }
          "GA EVENT" {
            string category
            string action
            string label
            string value
            string session
          }

          "TRAFFIC SOURCE" {
            String name
            bool isPaid
            float costPerC1ick
          }

          "ORDER LINE ITEM" {
            Product product
            Order order
            int  quantity
            float price
            float total
            float discount
            float tax
          }
