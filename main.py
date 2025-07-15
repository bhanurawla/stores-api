from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = FastAPI()

# Database connection parameters
DB_CONFIG = {
    "host": "aws-0-ap-southeast-1.pooler.supabase.com",
    "database": "postgres",
    "user": "postgres.oichgylkzbbvxgyxkldy", 
    "password": "Bhanu@100403",
    "port": 6543
}

@app.get("/stores")
def get_stores():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        cursor.execute("SELECT store, sales FROM stores_data")
        stores = cursor.fetchall()
        
        # Format as text
        result = []
        for store in stores:
            result.append(f"Store: {store['store']}, Monthly Sales: {store['sales']}")
        
        cursor.close()
        conn.close()
        
        return {"stores": result}
        
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
