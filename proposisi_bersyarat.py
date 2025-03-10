def implikasi (p,q):      
    return not p or q       

def konvers (p,q):          
    return implikasi (q,p)

def invers (p,q):
    return implikasi (not p, not q)

def kontraposisi (p, q):
    return implikasi (not q, not p)

def tabel_kebenaran() :
    print("\n")
    print("Tabel Kebenaran Prosisi Bersyarat")
    print("-" * 47)
    print("p\tq\tp->\tq->p\t~p->~q\t~q->~p")
    print("-" * 47)
    for p in [True,False]:
        for q in [True,False]:
            print(f"{p}\t{q}\t{implikasi(p,q)}\t{konvers(p,q)}\t{invers(p,q)}\t{kontraposisi(p,q)}")
tabel_kebenaran()
