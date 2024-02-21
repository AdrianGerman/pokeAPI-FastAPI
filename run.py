# archivo de ejecución
import uvicorn

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
