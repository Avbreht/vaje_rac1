# Problem trgovskega potnika

V nadaljevanju uporabljamo t.i. *MathJax* notacijo za Markdown. V VSCode urejevalniku jo omogočite z namestitvijo kakšne od naprednješih razširitev za Markdown (npr. `Markdown All in One`). 

---

V omrežju s petimi vozlišči imamo matriko uteži na usmerjenih povezavah.

$$
\begin{array}{c|ccccc}
  & 1 & 2 & 3 & 4 & 5 \\ \hline
1 & ∞ & 7 & 3 & 9 & 4 \\
2 & 5 & ∞ & 6 & 7 & 8 \\
3 & 3 & 4 & ∞ & 2 & 1 \\
4 & 9 & 3 & 7 & ∞ & 8 \\
5 & 1 & 4 & 2 & 5 & ∞ \\
\end{array}
$$

Oceno najkrajše poti dobimo z redukcijo matrike.

1. V vsakem stolpcu poiščemo minimum in shranimo njihovo vsoto. To je najmanjša cena, ki jo plačamo, da zapustimo vozlišča. Nato elementom v stolpcu odštejemo stolpični minimum.
2. V popravljeni matriki poiščemo vrstične minimume in shranimo vsoto. To je popravek glede na dejstvo, da moramo v vsako vozlišče tudi vstopiti. Elementom v vrstici odštejemo vrstične minimume.
3. Kot oceno vrnemo seštevek vsote stolpičnih minimumov in popravka (vsote vrstičnih minimumov v reducirani matriki).


Premislite:

1. Je pomembno, ali najprej gledamo stolpce in nato vrstice (poskrbimo za zapuščanje vozlišč in nato za prihod) ali pa vrstice in nato stolpce (poskrbimo za prihod in nato za odhod).
2. Kako izračunamo oceno, če smo se odločili, da mora biti povezava `1-2` prisotna v poti?
3. Izračunajte optimalno krožno pot v zgornjem omrežju. Če bo dovolj časa, izračunajte z obema variantama ocene (prihod->odhod in odhod->prihod) in primerjajte postopek.
