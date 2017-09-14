import numpy
import copy

class Doc(copy.deepcopy(list)):
    __pos_objet = []        # contient numero des objets
    __pos_objet_sommet = [] # contient position des sommet dans l'objet
    list_sommet = {}
    max_pos = list([-1, -1])
    min_pos = list([-1, -1])

    def ajoute_sommet(self, pos_xy, pos_objet, pos_objet_sommet):

        # tout sommet dans le document
        s = complex(pos_xy[0], pos_xy[1])
        try:
            self.list_sommet[s].append(tuple([pos_xy, pos_objet, pos_objet_sommet]))
        except KeyError:
            self.list_sommet[s] = []
            self.list_sommet[s].append(tuple([pos_xy, pos_objet, pos_objet_sommet]))

        super(self.__class__, self).append(pos_xy)
        self.__pos_objet.append(pos_objet)
        self.__pos_objet_sommet.append(pos_objet_sommet)

        if self.max_pos == [-1, -1] and self.min_pos == [-1, -1]:
            self.max_pos = list(copy.deepcopy(pos_xy))
            self.min_pos = list(copy.deepcopy(pos_xy))
        if self.max_pos[0] < pos_xy[0]:
            self.max_pos[0] = copy.deepcopy(pos_xy[0])
        if self.max_pos[1] < pos_xy[1]:
            self.max_pos[1] = copy.deepcopy(pos_xy[1])
        if pos_xy[0] < self.min_pos[0]:
            self.min_pos[0] = copy.deepcopy(pos_xy[0])
        if pos_xy[1] < self.min_pos[1]:
            self.min_pos[1] = copy.deepcopy(pos_xy[1])

    def supprimer_sommet(self, index):
        # supprimer un sommet du document
        self.__test_index(index)
        s = complex(super(self.__class__, self).__getitem__(index)[0],
                    super(self.__class__, self).__getitem__(index)[1])

        if self.list_sommet[s]:
            l = self.list_sommet[s]
            for i in l:
                if i[1] == self.__pos_objet[index] and i[2] == self.__pos_objet_sommet[index]:
                    del i
                    break
            #del self.list_sommet[s]

        super(self.__class__, self).__delitem__(index)
        del self.__pos_objet[index]
        del self.__pos_objet_sommet[index]

    def get_by_coord(self, coord):
        return self.list_sommet[complex(coord[0], coord[1])]

    def get(self, index):
        # avoir position xy du sommet + l'objet ou est contenu + position dans l'objet
        self.__test_index(index)
        return (super(self.__class__, self).__getitem__(index), self.__pos_objet[index], self.__pos_objet_sommet[index])

    def set(self, index, *arg):
        # modifier un sommet
        self.__test_index(index)
        arg = arg[0]
        if len(arg) == 3:
            s = complex(super(self.__class__, self).__getitem__(index)[0],
                        super(self.__class__, self).__getitem__(index)[1])
            super(self.__class__, self).__setitem__(index, arg[0])
            self.__pos_objet[index]          = arg[1]
            self.__pos_objet_sommet[index]   = arg[2]

            if self.list_sommet[s]:
                l = self.list_sommet[s]
                for i in l:
                    if i[1] == self.__pos_objet[index] and i[2] == self.__pos_objet_sommet[index]:
                        del i
                        break

            s = complex(arg[0][0], arg[0][1])
            try:
                self.list_sommet[s].append(tuple([arg[0], arg[1], arg[2]]))
            except KeyError:
                self.list_sommet[s] = []
                self.list_sommet[s].append(tuple([arg[0], arg[1], arg[2]]))
        else:
            raise Exception('Doc : number of arguments is not supported')

    def __test_index(self, index):
        if index < 0 or index > super(self.__class__, self).__len__()-1:
            raise Exception('Doc : index out of range')



