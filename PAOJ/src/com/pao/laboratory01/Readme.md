# Laboratory 01 — Clase, Încapsulare, Array-uri avansate


# bit.ly/4spF1HD

## Ce am învățat


### 1. Clase proprii — Încapsulare
O clasă grupează **date** (atribute) și **comportament** (metode) într-o singură unitate.

Regulile încapsulării:
- Atributele sunt `private` — nu pot fi accesate direct din exterior.
- Accesul se face prin **getteri** (citire) și **setteri** (scriere).
- **Constructorul** inițializează obiectul cu valori.
- `toString()` oferă o reprezentare text — se apelează automat la `System.out.println`.

```java
public class Dog {
    private String name;           // atribut privat
    private String color;

    public Dog(String name, String color) {   // constructor parametrizat
        this.name = name;
        this.color = color;
    }

    public String getName() { return name; }          // getter
    public void setName(String name) { this.name = name; }  // setter

    @Override
    public String toString() { return "Dog{name='" + name + "', color='" + color + "'}"; }
}
```

### 2. Subpachete — organizare cod
Clasele se grupează în subpachete după rol:
- `model/` — clasele de date (Dog, Cat, Car)
- `utils/` — clase utilitare (comparatori)
- `exercise/` — exercițiul de rezolvat

Când folosești o clasă din alt subpachet, o imporți:
```java
import com.pao.laboratory01.model.Dog;
```

### 3. Array-uri — redimensionare dinamică
Array-urile au dimensiune **fixă**. Ca să "adăugăm" un element:
1. Creăm un array nou cu `length + 1`.
2. Copiem elementele vechi cu `System.arraycopy`.
3. Punem noul element pe ultima poziție.

```java
int[] tmp = new int[arr.length + 1];
System.arraycopy(arr, 0, tmp, 0, arr.length);
tmp[tmp.length - 1] = valoareNoua;
```

### 4. Sortare cu `Comparator`
`Arrays.sort(array, comparator)` sortează un array de obiecte după o regulă definită de noi.

```java
Arrays.sort(dogs, new DogComparator());
```

`Comparator` este o clasă separată care implementează metoda `compare` — returnează negativ, 0, sau pozitiv.

### 5. Singleton Pattern
O clasă cu o **singură instanță** în toată aplicația.
- Constructorul este `private`.
- Se accesează prin `getInstance()`.
- Util pentru servicii centrale (ex: un depozit unic de date).

---

## Fișiere din acest laborator

| Fișier | Rol | Deschide |
|--------|-----|----------|
| [Main.java](Main.java) | **Demo** — instanțiere obiecte, import din model/, array de obiecte | ⬅ Citește codul |
| [model/Dog.java](model/Dog.java) | **Demo** — clasă completă cu încapsulare (referință) | ⬅ Citește și înțelege |
| [model/Cat.java](model/Cat.java) | **Demo** — al doilea model, structură identică | ⬅ Compară cu Dog |
| [arrays/ArrayDemo.java](arrays/ArrayDemo.java) | **Demo** — parcurgere, redimensionare, sortare | ⬅ Citește și rulează |
| [utils/DogComparator.java](utils/DogComparator.java) | **Demo** — Comparator extern pentru sortare | ⬅ Citește |
| [exercise/Car.java](exercise/Car.java) | **Exercițiu** — model Car (dat, citește-l) | ⬅ Înțelege structura |
| [exercise/CarService.java](exercise/CarService.java) | **Exercițiu** — Singleton cu TODO la bonus | ⬅ Completează `addReview` |
| [exercise/Main.java](exercise/Main.java) | **Exercițiu** — meniu interactiv cu TODO | ⬅ Completează cazul 3 |

---

## Ordinea recomandată

1. 📖 Citește [model/Dog.java](model/Dog.java) — înțelege încapsularea (private, getteri, setteri, toString).
2. 📖 Citește [model/Cat.java](model/Cat.java) — observă că structura e identică.
3. ▶️ Rulează [Main.java](Main.java) — vezi cum se creează și se afișează obiecte.
4. ▶️ Rulează [arrays/ArrayDemo.java](arrays/ArrayDemo.java) — vezi parcurgere, redimensionare, sortare.
5. 📖 Citește [utils/DogComparator.java](utils/DogComparator.java) — înțelege cum funcționează Comparator.
6. 🛠️ Rezolvă exercițiul din [exercise/](exercise/).

---

## Exercițiu — Sistem de gestionare mașini
📄 **Pachet:** [exercise/](exercise/)

Un sistem CRUD (Create, Read) pentru mașini, cu meniu interactiv.

> `Car` are: **name**, **color**, **reviews** (array de String-uri, inițial gol).
>
> `CarService` este un **Singleton** care gestionează un array intern de `Car[]`.
>
> Meniu:
> 1. **Listare** — afișează toate mașinile
> 2. **Adăugare** — citește name + color, creează și adaugă o mașină
> 3. **Adăugare review** *(bonus)* — caută o mașină după nume și îi adaugă un review
> 0. **Ieșire**

**Ce trebuie să faci:**
1. Citește [exercise/Car.java](exercise/Car.java) — înțelege structura modelului.
2. Citește [exercise/CarService.java](exercise/CarService.java) — înțelege Singleton-ul și metodele existente.
3. ✏️ Completează metoda `addReview` din [exercise/CarService.java](exercise/CarService.java).
4. ✏️ Completează cazul 3 din switch-ul din [exercise/Main.java](exercise/Main.java).

**Indicii:**
- Uită-te la `addCar` — pattern-ul de redimensionare este identic pentru reviews.
- Parcurge `cars` cu un `for` și compară cu `cars[i].getName().equals(carName)`.
- Ia array-ul curent cu `cars[i].getReviews()`, creează unul nou mai mare, copiază + adaugă, setează cu `setReviews`.

---

## Cum rulez?
1. **Demo-urile** — deschide `Main.java` sau `arrays/ArrayDemo.java` → click dreapta pe `main` → **Run**.
2. **Exercițiul** — deschide `exercise/Main.java` → click dreapta pe `main` → **Run** → interacționează cu meniul din consolă.

---

## Recapitulare rapidă

| Concept | Ce trebuie să rețin |
|---------|---------------------|
| Clasă | Atribute `private` + constructor + getteri/setteri + `toString` |
| Subpachete | `model/`, `utils/`, `exercise/` — organizează codul după rol |
| `import` | Necesar când folosești o clasă din alt (sub)pachet |
| Array redimensionare | `new int[length+1]` + `System.arraycopy` + element nou pe ultima poziție |
| `Comparator` | Clasă externă cu `compare()` — folosită de `Arrays.sort` |
| Singleton | Constructor `private`, acces prin `getInstance()`, o singură instanță |

---

## Ce urmează la Laboratory 02?
- Moștenire (`extends`, `super`)
- Clase abstracte și interfețe
- `equals` / `hashCode`
- Clase imutabile (`final`)
- `String` vs `StringBuilder` vs `StringBuffer`
- Colecții (`List`, `Set`)

